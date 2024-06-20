---
title: البدء
type: docs
weight: 5
url: /ar/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "إعداد Aspose.Cells لـ Node.js via Java وإرشادات التثبيت."
---

## **متطلبات النظام**
Aspose.Cells for Node.js via Java هو واجهة برمجية مستقلة عن المنصة ويمكن استخدامها على أي منصة (Windows، Linux و MacOS) حيث تم تثبيت [Node.js](https://nodejs.org/en/download/) وجسر [node-java](https://github.com/joeferner/node-java). يجب أن يكون لديك Oracle JDK بإصدار 7 أو أحدث قبل تثبيت التطبيق.
## **التثبيت من NPM**
يمكنك استخدام Aspose.Cells for Node.js via Java بسهولة من [NPM](https://www.npmjs.com/package/aspose.cells) باستخدام الأمر التالي.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

إذا واجهت أي مشاكل أثناء عملية التثبيت، يرجى الرجوع إلى https://www.npmjs.com/package/java.

## **التثبيت من أرشيف ZIP**
لتثبيت واستخدام Aspose.Cells for Node.js via Java من أرشيف ZIP، اتبع التعليمات التالية:
### **Linux:**
- قم بتنزيل وتثبيت [Node.js](https://nodejs.org/en/download/).
- قم بتثبيت Oracle JDK (1.7 أو 1.8) لنظام Linux، وقم بتكوين متغير البيئة JAVA_HOME.
- قم بتثبيت python 2.x
- قم بتثبيت [node-java](https://github.com/joeferner/node-java) bridge. يمكنك تشغيل الأوامر التالية في الطرفية: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- قم بتنزيل "Aspose.Cells for Node.js via Java" واستخراجه في "aspose.cells.js.java/node_modules".
- أنشئ ملف اختبار بالاسم **hello.js** باستخدام الكود النموذجي التالي في مجلد "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- الآن قم بتشغيل "node hello.js" في سطر الأوامر لتشغيله.
### **Windows:**
- قم بتثبيت Oracle JDK8 وقم بتكوين متغير البيئة JAVA_HOME.
- قم بتثبيت Node.js وأضف node.exe إلى المسار.
- قم بتثبيت node-gyp.
- قم بتثبيت أدوات بناء Windows.
- قم بتثبيت [جسر node-java](https://www.npmjs.com/package/java) وتشغيل الأوامر التالية في سطر الأوامر كمسؤول:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- قم بتنزيل "Aspose.Cells for Node.js via Java" واستخراجه في "aspose.cells.js.java/node_modules".
- قم بإنشاء ملف بالاسم **hello.js** في مجلد "aspose.cells.js.java" باستخدام رمز العينة التالي:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- الآن قم بتشغيل "node hello.js" في سطر الأوامر لتشغيله.
### **Mac:**
- قم بتنزيل وتثبيت Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- قم بتثبيت Oracle JDK 1.8 (الموصى به) لنظام Mac، قم بتكوين متغير البيئة JAVA_HOME.
- Modify <key>قدرات JVM</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



{{< highlight java >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- قم بتثبيت python 2.x (إذا لم يكن مثبتًا بالفعل).
- قم بتثبيت جسر node-java. يمكنك تشغيل الأوامر التالية في التيرمينال:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- قم بتنزيل "Aspose.Cells for Node.js via Java" واستخراجه في "aspose.cells.js.java/node_modules".
- قم بإنشاء ملف اختبار بالاسم **hello.js** باستخدام رمز العينة التالي في مجلد "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- الآن قم بتشغيل "node hello.js" في سطر الأوامر لتشغيله.

