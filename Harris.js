import download from "download";

const GetURL = (court, startDate, endDate) => {
  const date0 = startDate.split("/").join("%2F");
  const date1 = endDate.split("/").join("%2F");
  return `https://jpwebsite.harriscountytx.gov/PublicExtracts/GetExtractData?extractCaseType=CV&extract=6&court=${court}&casetype=EV&format=csv&fdate=${date0}&tdate=${date1}`;
};

const GetCSV = (court, startDate, endDate, uniq) => {
  const filename = `Harris-${uniq}.csv`;

  const url = GetURL(court, startDate, endDate);
  download(url, "tmp_csvs", { filename });
};

const strify = (startDate, endDate, court) => {
  return `${startDate.split("/").join("")}${endDate
    .split("/")
    .join("")}${court}`;
};

const GetAllCSVs = (dateArr) => {
  const startDate = dateArr[0];
  const endDate = dateArr[1];
  const courts = [
    "305",
    "310",
    "315",
    "320",
    "325",
    "330",
    "335",
    "340",
    "345",
    "350",
    "355",
    "360",
    "365",
    "370",
    "375",
    "380",
  ];

  for (let court of courts) {
    const uniq = strify(startDate, endDate, court);
    GetCSV(court, startDate, endDate, uniq);
  }
};

const DateStr = process.argv.slice(2)[0];
const DateArr = DateStr.split("_").map((e) => e.split("-"));
DateArr.map((dateArr) => {
  GetAllCSVs(dateArr);
});
