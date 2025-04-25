# 🤗 팀명 : Rolling
 
### 🤭 팀원

<p align="center">
  <table>
	<tr>
	  <td align="center">
		<img src="https://pbs.twimg.com/media/D07FPC9WwAYZ1k1.jpg" width="160" height="160"/><br>오종수 <p> O Jong Su  <p> [팀장] Team Manager
	  </td>
	  <td align="center">
		<img src="https://upload3.inven.co.kr/upload/2020/04/15/bbs/i13843617916.jpg" width="160" height="160"/><br>김효은 <p> Kim Hyo Eun
	  </td>
	  <td align="center">
		<img src="https://i.namu.wiki/i/CFdrduUAhyuiXzPMZ-WKsUJtGCuWOvzYLcIAdrcjZ2D7x4q3W1TxkGIYmBKTohKEM1vUNtgeZtilVHwCe2q17g.webp" width="160" height="160"/><br>박병헌 <p>Park Byung Hun
	  </td>
	  <td align="center">
		<img src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon4895.jpg?image=e_upscale,q_auto:good,f_webp,w_auto&v=1729058249" width="160" height="160"/><br>김정훈 <p> Kim Jeong Hun
	  </td>
	  <td align="center">
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-N5LKksvNwRIUWWcxuqWD2s52XO84KSOtdg&s" width="160" height="160"/><br>이지수 <p> Lee Ji Su
	  </td>
	</tr>
  </table>
</p>

### 💼 Role

### 👨‍💻 김정훈 Kim Jeong Hun
- **Backend**:  Migrated Streamlit page to Django (collaborative work)
- **Frontend**: Converted Streamlit page to HTML format (collaborative work)
- **tTest Code** : Wrote test code for the implemented page
### 👨‍💻 박병헌 Park Byung Hun
- **Detailed Page Design** : Wrote detailed page design document for Django migration
- **Backend**:  Migrated Streamlit page to Django (collaborative work)
- **Frontend**: Converted Streamlit page to HTML format (collaborative work)	
- **README** : Authored the README file

### 👩‍💻 이지수 Lee Ji Su
- **Requirements Specification:** : Authored the requirement specification document for Django migration
- **AWS Deployment**: Deployed the Django-based page on AWS

### 👨‍💻 오종수 O Jong Su
- **Team Leader**

---

## Project Overview
- **Detailed page design document creation**
- **Requirement specification document creation**
- **Migration from Streamlit to Django** 
- **Deployment on AWS**


This project involves crawling laptop product information from the Danawa site to build an **i**nteractive chatbot** that provides **hallucination-free** answers to user queries. The chatbot, originally built in Streamlit, was **migrated to Django and deployed**.

## Data

- Laptop data was collected via Selenium from the Danawa website (https://prod.danawa.com/list/?cate=112758).
<br>
- Collected data: Laptop model name, detailed specifications, price


## Preprocess

- The data saved as a CSV file was loaded into a document format, with metadata added and unnecessary characters in the contents removed for cleaning.
<br>
- The cleaned data was embedded and stored in Faiss DB using the 'text-embedding-3-small' model.

---



## Tech Stack

| Data Modeling | SCM | Front-End / Back-End | Deploy |
|-----------------|--------|---------------------|------------------|
| ![BeautifulSoup](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"><img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">|<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>| <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white">

## Prerequisites



### Create and Activate Conda Environment
```
conda env create -f environment.yml
conda activate best_laptop_env
```
---

### Required .env file 

<p>

```
OPENAI_API_KEY ="sk-*******************************************************************"
faiss_path ="./data/db"
```

### Required .env.prod file
```
DEBUG=0
SECRET_KEY=****************************************
DJANGO_ALLOWED_HOSTS=localhost ******************* [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=****
SQL_HOST=best-laptop.c****************************
SQL_PORT=5432
```
### Required .env.prod.db file
```
POSTGRES_USER=************************
POSTGRES_PASSWORD=***************************************
POSTGRES_DB=**************************
```


## Usage

After launching an EC2 instance on AWS, run the following commands:
```cmd
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py collectstatic
```
```cmd
Access via your EC2 IP address
```

## System Architecture

<p>
  <img src="readmeImage/Architecture.png" alt="이미지 설명" width="500" height="350">
</p>

Our system embeds data crawled via Selenium into FAISS (Vector DB) for vector-based search.
User questions pass through a retriever and chain model, and our custom model generates responses.
The final results are intuitively presented to users through the deployed web page.
 
---
## Test Case

### Incorrect question example
<img src="readmeImage\test1.png" alt="이미지 설명" width="" height="500">
<img src="readmeImage\test2.png" alt="이미지 설명" width="" height="500">

### Correct question example
<img src="readmeImage\test3.png" alt="이미지 설명" width="" height="500">


## Result

**Requirement Specification Document**
<p>
  <img src="readmeImage\SRS.png" alt="이미지 설명" width="" height="200">
</p>

**Detailed Page Design**
<p>
  <img src="readmeImage\detailpagestructre.png" alt="이미지 설명" width="500" height="350">
</p>


<br>
**Deployed Django Page**
<p>
  <img src="readmeImage\page.png" alt="이미지 설명" width="500" height="350">
</p>

Reflecting the requirement specification and detailed page design, we built the front-end and back-end using Django and deployed it via AWS.

## Final Thoughts


### 👨‍💻 김정훈 Kim Jeong Hun
- Writing test cases and contributing to various tasks was a great opportunity for personal growth.

### 👨‍💻 박병헌 Park Byung Hun
- I initially thought migrating from Streamlit to Django would be easy, but faced challenges in Django backend work. However, with teamwork, we overcame them. Connecting this with the previous project gave me a great sense of achievement.
### 👩‍💻 이지수 Lee Ji Su
- I was in charge of configuring the AWS environment. Successfully running a web page on AWS was a valuable experience and will serve as a solid foundation for real-world applications.

### 👨‍💻 오종수 O Jong Su 
- Achieving our goal as a team was a very meaningful experience.