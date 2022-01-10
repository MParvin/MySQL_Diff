# MySQL_Diff
Find differents between MySQL master,slave or master,master databases.

To use this program just copy `.env.example` to `.env`
```
cp .env.example .env
```

Edit `.env` and put your database credentials.

Install dependencies:
```
pip install -r requirements.txt
```
*** Use [virtualenv](https://pypi.org/project/virtualenv/)

Run the program:
```
python main.py
```

I recommened you use [screen](https://linux.die.net/man/1/screen), if you have a large database.
