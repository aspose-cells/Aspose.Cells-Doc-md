---
title: Начало работы
type: docs
weight: 5
url: /ru/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "настройка Aspose.Cells для Node.js via Java и руководство по установке."
---

## **Системные требования**
Aspose.Cells для Node.js via Java — это API, независимое от платформы, которое можно использовать на любой платформе (Windows, Linux и MacOS), где установлены [Node.js](https://nodejs.org/en/download/) и мост [node-java](https://github.com/joeferner/node-java). Перед установкой на машине должны быть установлены Oracle JDK версий 7 или выше.
## **Установка из NPM**
Вы можете легко использовать Aspose.Cells для Node.js via Java из [NPM](https://www.npmjs.com/package/aspose.cells) с помощью следующей команды.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Если у вас возникли проблемы во время процесса установки, обратитесь по адресу https://www.npmjs.com/package/java.

## **Установка из ZIP-архива**
Чтобы установить и использовать Aspose.Cells для Node.js via Java из ZIP-архива, следуйте следующим инструкциям:
### **Linux:**
- Скачайте и установите [Node.js](https://nodejs.org/en/download/).
- Установите Oracle JDK (1.7 или 1.8) для Linux, настройте переменную среды JAVA_HOME.
- Установите Python 3.x
- Установите [мост node-java](https://github.com/joeferner/node-java) bridge. Вы можете выполнить нижеуказанные команды в терминале: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Загрузите "Aspose.Cells для Node.js via Java" и извлеките его в папку "aspose.cells.js.java/node_modules".
- Создайте тестовый файл с именем **hello.js** с использованием следующего образца кода в папке "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Теперь запустите "node hello.js" @ command prompt, чтобы выполнить его.
### **Windows:**
- Установите Oracle JDK8 и настройте переменную среды JAVA_HOME.
- Установите Node.js и добавьте node.exe в PATH.
- Установите Python и добавьте его в PATH.
- Установите node-gyp.
- Установите [мост node-java](https://www.npmjs.com/package/java).
- Установите aspose.cells (ИЛИ: скачайте "Aspose.Cells for Node.js via Java" и распакуйте его в "aspose.cells.js.java/node_modules").

Выполните команды ниже @ командной строке от имени администратора (**Убедитесь, что Java, Node.js, Python настроены**):

{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install java

\> npm install aspose.cells

{{< /highlight >}}

- Создайте файл с именем **hello.js** в папке "aspose.cells.js.java" с использованием следующего образца кода:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Теперь запустите "node hello.js" @ command prompt, чтобы выполнить его.
### **Mac:**
- Загрузите и установите Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Установите Oracle JDK 1.8 (рекомендуется) для Mac, настройте переменную среды JAVA_HOME.
- Modify <key>JVMCapabilities</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



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



- Установите Python 3.x (если он не установлен).
- Установите мост node-java. Вы можете выполнить нижеприведенные команды @ terminal:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Загрузите "Aspose.Cells для Node.js via Java" и извлеките его в папку "aspose.cells.js.java/node_modules".
- Создайте тестовый файл с именем **hello.js** с использованием следующего образца кода в папке "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Затем запустите "node hello.js" в командной строке для его выполнения.

