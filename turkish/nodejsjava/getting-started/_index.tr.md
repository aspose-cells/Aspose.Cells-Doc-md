---
title: Başlarken
type: docs
weight: 5
url: /tr/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "Node.js için Aspose.Cells via Java ü kurma ve kurulum kılavuzları."
---

## **Sistem Gereksinimleri**
Aspose.Cells for Node.js via Java platform bağımsız bir API'dir ve [Node.js](https://nodejs.org/en/download/) ve [node-java](https://github.com/joeferner/node-java) köprüsünün kurulu olduğu herhangi bir platformda (Windows, Linux ve MacOS) kullanılabilir. Makinede, kurulumu ayarlamadan önce Oracle JDK 7 veya daha yeni sürümlerin yüklü olması gerekir.
## **NPM'den Kurulum**
Aşağıdaki komutla [NPM](https://www.npmjs.com/package/aspose.cells) üzerinden Aspose.Cells for Node.js via Java'ü kolayca kullanabilirsiniz.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Kurulum süreci sırasında herhangi bir sorunla karşılaşırsanız, lütfen https://www.npmjs.com/package/java adresine başvurun.

## **ZIP arşivinden Kurulum**
Aspose.Cells for Node.js via Java'ü ZIP arşivinden kurmak ve kullanmak için aşağıdaki talimatları izleyin:
### **Linux:**
- [Node.js](https://nodejs.org/en/download/) indirin ve kurun.
- Linux için Oracle JDK (1.7 veya 1.8) yükleyin, JAVA_HOME ortam değişkenini yapılandırın.
- Python 3.x yükleyin
- [node-java köprüsü](https://github.com/joeferner/node-java) indirin ve kurun. Aşağıdaki komutları terminalde çalıştırabilirsiniz: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- "Aspose.Cells for Node.js via Java"'ü indirin ve "aspose.cells.js.java/node_modules" dizinine çıkarın.
- "aspose.cells.js.java" klasöründe aşağıdaki örnek kodu kullanarak **hello.js** adında bir test dosyası oluşturun:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi "node hello.js" komut istemine çalıştırın.
### **Windows:**
- Oracle JDK8'i indirin ve JAVA_HOME ortam değişkenini yapılandırın.
- Node.js'i kurun ve node.exe'yi PATH'a ekleyin.
- Python yükleyin ve PATH'e ekleyin.
- node-gyp kurulumu yapın.
- [node-java köprüsü](https://www.npmjs.com/package/java) yükleyin.
- aspose.cells yükleyin (VEYA: "Aspose.Cells for Node.js via Java" dosyasını indirin ve "aspose.cells.js.java/node_modules" klasörüne çıkartın).

Aşağıdaki komutları yönetici olarak komut istemcisinde çalıştırın (**Java, Node.js, Python yapılandırıldığından emin olun**):

{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install java

\> npm install aspose.cells

{{< /highlight >}}

- "aspose.cells.js.java" klasöründe aşağıdaki örnek kodu kullanarak **hello.js** adında bir dosya oluşturun:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi "node hello.js" komut istemine çalıştırın.
### **Mac:**
- Node.js'i indirin ve kurun ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Mac için Oracle JDK 1.8 (tavsiye edilen) kurun ve JAVA_HOME ortam değişkenini yapılandırın.
- Modify <key>JVMYetenekleri</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



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



- Python 3.x i yükleyin (yüklenmediyse).
- node-java köprüsünü indirin ve kurun. Aşağıdaki komutları terminalde çalıştırabilirsiniz:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- "Aspose.Cells for Node.js via Java"'ü indirin ve "aspose.cells.js.java/node_modules" dizinine çıkarın.
- "aspose.cells.js.java" klasöründe aşağıdaki örnek kodu kullanarak **hello.js** adında bir test dosyası oluşturun:



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Şimdi "node hello.js" komut istemine çalıştırın.

