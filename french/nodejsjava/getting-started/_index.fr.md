---
title: Commencer
type: docs
weight: 5
url: /fr/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: configuration Aspose.Cells pour Node.js via Java et directives d'installation
---
## **Configuration requise**
 Aspose.Cells pour Node.js via Java est indépendant de la plate-forme API et peut être utilisé sur n'importe quelle plate-forme (Windows, Linux et MacOS) où[Node.js](https://nodejs.org/en/download/) et[noeud-java](https://github.com/joeferner/node-java)pont sont installés. La machine doit avoir Oracle JDK 7 ou des versions supérieures avant de configurer l'installation.
## **Installer à partir de NPM**
 Vous pouvez facilement utiliser Aspose.Cells pour Node.js via Java à partir de[MNP](https://www.npmjs.com/package/aspose.cells) avec la commande suivante.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Si vous rencontrez des problèmes lors du processus d'installation, veuillez vous référer à https://www.npmjs.com/package/java.

## **Installer à partir de l'archive ZIP**
Pour installer et utiliser Aspose.Cells pour Node.js via Java à partir d'une archive ZIP, suivez les instructions suivantes :
### **Linux :**
-  Télécharger et installer[Node.js](https://nodejs.org/en/download/).
- Installez Oracle JDK (1.7 ou 1.8) pour Linux, configurez la variable d'environnement JAVA_HOME.
- Installer Python 2.x
-  Installer[noeud-java](https://github.com/joeferner/node-java) pont. Vous pouvez exécuter les commandes ci-dessous @ terminal :



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Téléchargez "Aspose.Cells pour Node.js via Java" et extrayez-le dans "aspose.cells.js.java/node_modules".
- Créez un fichier de test nommé**bonjour.js**en utilisant l'exemple de code suivant dans le dossier "aspose.cells.js.java":

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Exécutez maintenant "node hello.js" @invite de commande pour l'exécuter.
### **Windows:**
- Installez Oracle JDK8 et configurez la variable d'environnement JAVA_HOME.
- Installez Node.js et ajoutez node.exe à PATH.
- Installez node-gyp.
- Installez les outils de construction Windows.
-  Installer[pont noeud-java](https://www.npmjs.com/package/java) et exécutez les commandes ci-dessous à l'invite de commande en tant qu'administrateur :



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Téléchargez "Aspose.Cells pour Node.js via Java" et extrayez-le dans "aspose.cells.js.java/node_modules".
-  Créer un fichier nommé**bonjour.js**dans le dossier "aspose.cells.js.java" en utilisant l'exemple de code suivant :

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Exécutez maintenant "node hello.js" @invite de commande pour l'exécuter.
### **Mac:**
- Téléchargez et installez Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installez Oracle JDK 1.8 (recommandé) pour Mac, configurez la variable d'environnement JAVA_HOME.
-  Modifier<key>Capacités JVM</key> section dans "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" avec le privilège root. ("jdk1.8.0_152.jdk" dépend de votre version de jdk), faites-le ressembler à ceci :



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



- Installez Python 2.x (s'il n'est pas installé).
- Installez le pont nœud-java. Vous pouvez exécuter les commandes ci-dessous @ terminal :

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm installer java

- Téléchargez "Aspose.Cells pour Node.js via Java" et extrayez-le dans "aspose.cells.js.java/node_modules".
-  Créez un fichier de test nommé**bonjour.js** en utilisant l'exemple de code suivant dans le dossier "aspose.cells.js.java":



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Exécutez maintenant "node hello.js" @invite de commande pour l'exécuter.

