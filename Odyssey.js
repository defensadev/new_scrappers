import puppeteer from "puppeteer";
import fs from "fs";

const writeToJSON = (x) => {
  fs.writeFile("FormData.json", JSON.stringify(x), "utf8", () => {});
};

const main = async () => {
  const rt = [];

  const browser = await puppeteer.launch();

  const page = await browser.newPage();

  await page.setRequestInterception(true);

  page.on("request", async (request) => {
    try {
      const postdata = await request.postData();
      const JSONPostData = JSON.parse(
        '{"' + postdata.replace(/&/g, '","').replace(/=/g, '":"') + '"}',
        function (key, value) {
          return key === "" ? value : decodeURIComponent(value);
        }
      );

      if ("__EVENTTARGET" in JSONPostData) {
        rt.push(JSONPostData);
      }
    } catch (err) {}
    request.continue();
  });

  await page.goto(
    "https://odyssey.tarrantcounty.com/PublicAccess/default.aspx"
  );

  await page.select(
    "#sbxControlID2",
    "400,401,402,403,404,405,406,407,408,409"
  );

  await page.click(
    "body > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > a:nth-child(10)"
  );

  await page.waitForSelector("#SearchBy");

  await page.select("#SearchBy", "5");

  await page.click("#chkDtRangeCriminal");
  await page.click("#chkDtRangeFamily");
  await page.click("#chkDtRangeProbate");

  await page.click("#SearchSubmit");

  await browser.close();

  return rt;
};

main().then((res) => writeToJSON(res[0]));
