import shutil, os

if __name__ == "__main__":
    shutil.rmtree('tmp_csvs')
    os.mkdir('tmp_csvs')