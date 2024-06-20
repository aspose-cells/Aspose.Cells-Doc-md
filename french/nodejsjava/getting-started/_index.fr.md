---
title: Pour commencer
type: docs
weight: 5
url: /fr/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "configurer Aspose.Cells pour Node.js via Java et les directives d installation."
---

## **Configuration requise**
Aspose.Cells for Node.js via Java est une API multiplateforme et peut être utilisée sur n'importe quelle plateforme (Windows, Linux et MacOS) où [Node.js](https://nodejs.org/en/download/) et le pont [node-java](https://github.com/joeferner/node-java) sont installés. La machine doit disposer d'Oracle JDK 7 ou de versions supérieures avant de procéder à l'installation.
## **Installation à partir de NPM**
Vous pouvez facilement utiliser Aspose.Cells for Node.js via Java à partir de [NPM](https://www.npmjs.com/package/aspose.cells) avec la commande suivante.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Si vous rencontrez des problèmes lors du processus d'installation, veuillez vous référer à https://www.npmjs.com/package/java.

## **Installation à partir de l'archive ZIP**
Pour installer et utiliser Aspose.Cells for Node.js via Java à partir d'une archive ZIP, suivez les instructions suivantes :
### **Linux:**
- Téléchargez et installez [Node.js](https://nodejs.org/en/download/).
- Installez Oracle JDK (1.7 ou 1.8) pour Linux, configurez la variable d'environnement JAVA_HOME.
- Installez python 2.x
- Installez le pont [node-java](https://github.com/joeferner/node-java). Vous pouvez exécuter les commandes suivantes dans le terminal : 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Téléchargez "Aspose.Cells for Node.js via Java" et extrayez-le dans le dossier "aspose.cells.js.java/node_modules".
- Créez un fichier de test nommé **hello.js** en utilisant le code source suivant dans le dossier "aspose.cells.js.java" :

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Maintenant, exécutez "node hello.js" depuis l'invite de commande pour le lancer.
### **Windows:**
- Installez Oracle JDK8 et configurez la variable d'environnement JAVA_HOME.
- Installez Node.js et ajoutez node.exe au PATH.
- Installez node-gyp.
- Installez Windows Build Tools.
- Installez le pont Java-Node ([node-java bridge](https://www.npmjs.com/package/java)) et exécutez les commandes ci-dessous depuis l'invite de commande en tant qu'administrateur :



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Téléchargez "Aspose.Cells for Node.js via Java" et extrayez-le dans le dossier "aspose.cells.js.java/node_modules".
- Créez un fichier nommé **hello.js** dans le dossier "aspose.cells.js.java" en utilisant le code d'exemple suivant :

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Maintenant, exécutez "node hello.js" depuis l'invite de commande pour le lancer.
### **Mac:**
- Téléchargez et installez Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installez Oracle JDK 1.8 (recommandé) pour Mac, configurez la variable d'environnement JAVA_HOME.
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



- Installez python 2.x (s'il n'est pas déjà installé).
- Installez le pont Java-Node. Vous pouvez exécuter les commandes ci-dessous dans le terminal :

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Téléchargez "Aspose.Cells for Node.js via Java" et extrayez-le dans le dossier "aspose.cells.js.java/node_modules".
- Créez un fichier de test nommé **hello.js** en utilisant le code d'exemple suivant dans le dossier "aspose.cells.js.java" :



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Maintenant, exécutez "node hello.js" depuis l'invite de commande pour le lancer.

