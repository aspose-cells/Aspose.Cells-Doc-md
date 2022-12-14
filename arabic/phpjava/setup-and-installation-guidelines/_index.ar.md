---
title: إرشادات الإعداد والتثبيت
type: docs
weight: 20
url: /ar/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: إعداد Aspose.Cells لـ PHP عبر Java وإرشادات التثبيت
---
## **متطلبات النظام**
Aspose.Cells لـ PHP عبر Java هو نظام أساسي مستقل API ويمكن استخدامه على أي منصة (Windows ، Linux ، MacOS ، إلخ) حيث[بي أتش بي](https://www.php.net/downloads.php)تم تثبيت 7 إصدارات أو أكبر. يجب أن يحتوي الجهاز على Oracle JDK 7 أو إصدارات أحدث قبل إعداد التثبيت.
## **التثبيت والاستخدام**
يتم توزيع Aspose.Cells لـ PHP عبر Java كأرشيف ZIP.

لإعداد البيئة ، قم بتثبيت واستخدام Aspose.Cells لـ PHP عبر Java ، اتبع التعليمات:
### **لينكس:**
- تحميل[بي أتش بي](https://www.php.net/downloads.php)المصدر وتثبيته. أو استخدم الأمر "sudo apt install php-xxx" لتثبيت php binary.
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام Linux ، قم بتكوين متغير بيئة JAVA_HOME.
- قم بتنزيل / احصل على "Aspose.Cells لـ PHP عبر Java" API واستخرجه. سيكون هناك مجلد باسم "aspose.cells".
- قم بتنزيل PHP / Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java / Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل "PHP / Java Bridge" في المجلد أعلاه باستخدام الأمر أدناه.

|جافا $_HOME / bin / java -Djava.ext.dirs = lib -jar JavaBridge.jar SERVLET_محلي: 8080> / dev / null 2> & 1 &|
|:- |
- شغّل "example.php" في مجلد "aspose.cells" لتشغيل المثال باستخدام الأمر التالي:

|php $ example.php|
|:- |
### **Windows:**
- تحميل[بي أتش بي](https://www.php.net/downloads.php)windows binary وإضافة "php.exe" إلى PATH.
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لـ Windows وقم بتكوين متغير بيئة JAVA_HOME.
- قم بتنزيل "Aspose.Cells لـ PHP عبر Java" API واستخرجه. سيكون هناك مجلد باسم "aspose.cells".
- قم بتنزيل PHP / Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java / Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل "PHP / Java Bridge" في المجلد أعلاه باستخدام الأمر أدناه. حدد منفذ الإصغاء 8080 http عند بدء الجسر وانقر فوق الزر "موافق".

|>٪ JAVA_HOME٪ / bin / java -Djava.ext.dirs = lib -jar JavaBridge.jar|
|:- |
- شغّل "example.php" في مجلد "aspose.cells" لتشغيل المثال باستخدام الأمر التالي:

|> php example.php|
|:- |
### **ماك:**
- تثبيت[بي أتش بي](https://www.php.net/downloads.php).
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام التشغيل Mac ، وقم بتكوين متغير بيئة JAVA_HOME.
- قم بتنزيل "Aspose.Cells لـ PHP عبر Java" API واستخرجه. سيكون هناك مجلد باسم "aspose.cells".
- قم بتنزيل PHP / Java Bridge binary (JavaBridge.jar) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظه في مجلد "aspose.cells".
- قم بتنزيل مكتبة java / Java.inc PHP (Java.inc) من http://php-java-bridge.sourceforge.net/pjb/download.php واحفظها في مجلد "aspose.cells".
- قم بتشغيل "PHP / Java Bridge" في المجلد أعلاه باستخدام الأمر أدناه. حدد منفذ الإصغاء 8080 http عند بدء الجسر وانقر فوق الزر "موافق".

|$ JAVA_HOME / bin / java -Djava.ext.dirs = lib -jar JavaBridge.jar|
|:- |
- شغّل "example.php" في مجلد "aspose.cells" لتشغيل المثال باستخدام الأمر التالي:

|php $ example.php|
|:- |


