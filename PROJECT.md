# shotsort

## What it does
shotsort is an app that helps people find old screenshots. You upload
screenshots, and the app reads the text in each one using OCR so you can
search by what it says. It also uses a machine learning model to
automatically tag each screenshot (for example, receipt or chat). If a
tag is wrong, you can correct it, and the app uses those corrections to
retrain and improve the model. It is built for anyone with a camera roll
full of screenshots they can never find.

## Tag categories
- receipt
- chat
- code
- map
- meme
- other

## Screenshot record fields
- id
- file_name
- ocr_text
- predicted_tag
- corrected_tag
- uploaded_at
