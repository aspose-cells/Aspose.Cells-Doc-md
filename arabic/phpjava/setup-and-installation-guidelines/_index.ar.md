---
title: إرشادات الإعداد والتثبيت
type: docs
weight: 20
url: /ar/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "تثبيت Aspose.Cells for PHP via Java وإرشادات التثبيت."
---



## **متطلبات النظام**
Aspose.Cells for PHP via Java هو واجهة برمجة تطبيقات مستقلة عن المنصة ويمكن استخدامها على أي منصة (ويندوز، لينكس، ماك إلخ) حيث يتم تثبيت نسخ PHP 7 أو أحدث. يجب أن يحتوي الجهاز على Oracle JDK 7 أو أحدث قبل إعداد التثبيت.
## **التثبيت والاستخدام**
تُوزع Aspose.Cells for PHP via Java كأرشيف ZIP.

لإعداد البيئة وتثبيت واستخدام Aspose.Cells for PHP via Java، اتبع التعليمات:
### **Linux:**
- قم بتنزيل مصدر [PHP](https://www.php.net/downloads.php) وقم بتثبيته. أو استخدم الأمر “sudo apt install php-xxx” لتثبيت نسخة من برنامج php.
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام Linux، وقم بتكوين متغير البيئة JAVA_HOME.
- قم بتنزيل/الحصول على واجهة برمجة تطبيقات "Aspose.Cells for PHP via Java" وقم بفك ضغطها. سيكون هناك مجلد يُسمى "aspose.cells".
- قم بتنزيل ملف PHP/Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java/Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل “PHP/Java Bridge” في المجلد أعلاه باستخدام الأمر التالي.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- قم بتشغيل "example.php" في مجلد "aspose.cells" لتشغيل المثال بالأمر التالي:

|$ php example.php|
| :- |
### **Windows:**
- قم بتنزيل ملف PHP الخاص بويندوز من [PHP](https://www.php.net/downloads.php) وأضف "php.exe" إلى PATH.
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام Windows وقم بتكوين متغير البيئة JAVA_HOME.
- قم بتنزيل API "Aspose.Cells for PHP via Java" واستخراجه. سيكون هناك مجلد يسمى "aspose.cells".
- قم بتنزيل ملف PHP/Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java/Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل ‏"PHP/Java Bridge" في المجلد أعلاه بالأمر التالي. حدد منفذ الاستماع http 8080 عند بدء الجسر وانقر على زر موافق.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- قم بتشغيل "example.php" في مجلد "aspose.cells" لتشغيل المثال بالأمر التالي:

|> php example.php|
| :- |
### **Mac:**
- قم بتثبيت [PHP](https://www.php.net/downloads.php).
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام Mac وقم بتكوين متغير البيئة JAVA_HOME.
- قم بتنزيل API "Aspose.Cells for PHP via Java" واستخراجه. سيكون هناك مجلد يسمى "aspose.cells".
- قم بتنزيل ملف PHP/Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java/Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل ‏"PHP/Java Bridge" في المجلد أعلاه بالأمر التالي. حدد منفذ الاستماع http 8080 عند بدء الجسر وانقر على زر موافق.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- قم بتشغيل "example.php" في مجلد "aspose.cells" لتشغيل المثال بالأمر التالي:

|$ php example.php|
| :- |


