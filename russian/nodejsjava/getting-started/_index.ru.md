---
title: Начиная
type: docs
weight: 5
url: /ru/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: настроить Aspose.Cells для Node.js через Java и руководство по установке
---
## **Системные Требования**
 Aspose.Cells для Node.js через Java не зависит от платформы API и может использоваться на любой платформе (Windows, Linux и MacOS), где[Node.js](https://nodejs.org/en/download/) а также[узел-java](https://github.com/joeferner/node-java)мост установлен. Перед настройкой установки на компьютере должна быть установлена версия Oracle JDK 7 или выше.
## **Установить из NPM**
 Вы можете легко использовать Aspose.Cells для Node.js через Java от[НПМ](https://www.npmjs.com/package/aspose.cells) с помощью следующей команды.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Если у вас возникнут какие-либо проблемы в процессе установки, обратитесь к https://www.npmjs.com/package/java.

## **Установить из ZIP-архива**
Чтобы установить и использовать Aspose.Cells для Node.js через Java из ZIP-архива, следуйте следующим инструкциям:
### **Линукс:**
-  Загрузить и установить[Node.js](https://nodejs.org/en/download/).
- Установите Oracle JDK (1.7 или 1.8) для Linux, настройте переменную среды JAVA_HOME.
- Установите питон 2.х
-  Установить[узел-java](https://github.com/joeferner/node-java) мост. Вы можете запустить следующие команды @ терминал:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Загрузите «Aspose.Cells для Node.js через Java» и извлеките его в «aspose.cells.js.java/node_modules».
- Создайте тестовый файл с именем**привет.js**используя следующий пример кода в папке «aspose.cells.js.java»:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Теперь запустите «node hello.js» в командной строке, чтобы запустить его.
### **Windows:**
- Установите Oracle JDK8 и настройте переменную среды JAVA_HOME.
- Установите Node.js и добавьте node.exe в PATH.
- Установите узел-гип.
- Установите Windows Инструменты сборки.
-  Установить[мост node-java](https://www.npmjs.com/package/java) и запустите следующие команды @ в командной строке от имени администратора:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Загрузите «Aspose.Cells для Node.js через Java» и извлеките его в «aspose.cells.js.java/node_modules».
-  Создайте файл с именем**привет.js**в папке «aspose.cells.js.java», используя следующий пример кода:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Теперь запустите «node hello.js» в командной строке, чтобы запустить его.
### **Мак:**
- Загрузите и установите Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Установите Oracle JDK 1.8 (рекомендуется) для Mac, настройте переменную среды JAVA_HOME.
-  Изменить<key>Возможности JVM</key> раздел в "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" с привилегиями root. ("jdk1.8.0_152.jdk" зависит от вашей версии jdk), сделайте так, чтобы он выглядел следующим образом:



{{< highlight "java" >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- Установите python 2.x (если он не установлен).
- Установите мост node-java. Вы можете запустить следующие команды @ терминал:

`         `$ mkdir aspose.cells.js.java

`         `$ компакт-диск aspose.cells.js.java

`         `$ npm установить Java

- Загрузите «Aspose.Cells для Node.js через Java» и извлеките его в «aspose.cells.js.java/node_modules».
-  Создайте тестовый файл с именем**привет.js** используя следующий пример кода в папке «aspose.cells.js.java»:



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Теперь запустите «node hello.js» в командной строке, чтобы запустить его.

