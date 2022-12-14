---
title: Başlarken
type: docs
weight: 5
url: /tr/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: Java üzerinden Node.js için Aspose.Cells kurulumu ve kurulum yönergeleri
---
## **sistem gereksinimleri**
 Java üzerinden Node.js için Aspose.Cells, platformdan bağımsız API'dir ve herhangi bir platformda (Windows, Linux ve MacOS) kullanılabilir.[Node.js](https://nodejs.org/en/download/) ve[düğüm-java](https://github.com/joeferner/node-java)köprü kurulur. Kurulumu kurmadan önce makinede Oracle JDK 7 veya üzeri sürümler bulunmalıdır.
## **NPM'den yükleyin**
 Node.js için Aspose.Cells'i Java üzerinden rahatlıkla kullanabilirsiniz.[NPM](https://www.npmjs.com/package/aspose.cells) aşağıdaki komutla.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Yükleme işlemi sırasında herhangi bir sorunla karşılaşırsanız, lütfen https://www.npmjs.com/package/java adresine bakın.

## **ZIP arşivinden yükleyin**
Bir ZIP arşivinden Java aracılığıyla Node.js için Aspose.Cells'i yüklemek ve kullanmak için aşağıdaki talimatları izleyin:
### **Linux:**
-  İndirin ve kurun[Node.js](https://nodejs.org/en/download/).
- Linux için Oracle JDK (1.7 veya 1.8) yükleyin, Java_HOME ortam değişkenini yapılandırın.
- Python 2.x'i kurun
-  Düzenlemek[düğüm-java](https://github.com/joeferner/node-java) köprü. Aşağıdaki komutları @ terminalde çalıştırabilirsiniz:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- "Aspose.Cells for Node.js via Java" dosyasını indirin ve "aspose.cells.js.java/node_modules" içine çıkarın.
- adlı bir test dosyası oluşturun.**merhaba.js**"aspose.cells.js.java" klasöründe aşağıdaki örnek kodu kullanarak:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi çalıştırmak için "node hello.js" @komut istemini çalıştırın.
### **Windows:**
- Oracle JDK8'i yükleyin ve Java_HOME ortam değişkenini yapılandırın.
- Node.js'yi kurun ve node.exe'yi PATH'e ekleyin.
- node-gyp'yi kurun.
- Windows Derleme Araçları'nı yükleyin.
-  Düzenlemek[düğüm-java köprüsü](https://www.npmjs.com/package/java) ve aşağıdaki komutları @ komut istemini yönetici olarak çalıştırın:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- "Aspose.Cells for Node.js via Java" dosyasını indirin ve "aspose.cells.js.java/node_modules" içine çıkarın.
-  adlı bir dosya oluşturun.**merhaba.js**aşağıdaki örnek kodu kullanarak "aspose.cells.js.java" klasöründe:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi çalıştırmak için "node hello.js" @komut istemini çalıştırın.
### **Mac:**
- Node.js'yi indirin ve kurun ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Mac için Oracle JDK 1.8'i kurun (önerilen), JAVA_HOME ortam değişkenini yapılandırın.
-  Değiştir<key>JVMCapabiliteleri</key> "/Library/Java/JavaVirtualMachines/jdk1.8.0" bölümünde_152.jdk/Contents/Info.plist", kök ayrıcalığına sahiptir. ("jdk1.8.0_152.jdk", jdk sürümünüze bağlıdır), aşağıdaki gibi görünmesini sağlayın:



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



- Python 2.x'i yükleyin (kurulu değilse).
- Node-java köprüsünü kurun. Aşağıdaki komutları @ terminalde çalıştırabilirsiniz:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm Java'yı kurun

- "Aspose.Cells for Node.js via Java" dosyasını indirin ve "aspose.cells.js.java/node_modules" içine çıkarın.
-  adlı bir test dosyası oluşturun.**merhaba.js** "aspose.cells.js.java" klasöründe aşağıdaki örnek kodu kullanarak:



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi çalıştırmak için "node hello.js" @komut istemini çalıştırın.

