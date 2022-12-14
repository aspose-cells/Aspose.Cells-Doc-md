---
title: Consignes de configuration et d'installation
type: docs
weight: 20
url: /fr/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: configuration Aspose.Cells pour PHP via Java et directives d'installation
---
## **Configuration requise**
Aspose.Cells pour PHP via Java est indépendant de la plate-forme API et peut être utilisé sur n'importe quelle plate-forme (Windows, Linux, MacOS, etc.) où[PHP](https://www.php.net/downloads.php)ou des versions supérieures sont installées. La machine doit avoir Oracle JDK 7 ou des versions supérieures avant de configurer l'installation.
## **Installation et utilisation**
Aspose.Cells pour PHP via Java est distribué sous forme d'archive ZIP.

Pour configurer l'environnement, installez et utilisez Aspose.Cells pour PHP via Java, suivez les instructions :
### **Linux :**
- Télécharger[PHP](https://www.php.net/downloads.php)source et installez-le. Ou, utilisez la commande "sudo apt install php-xxx" pour installer le binaire php.
- Installez Oracle JDK (1.7 ou 1.8) pour Linux, configurez la variable d'environnement JAVA_HOME.
- Téléchargez/obtenez "Aspose.Cells pour PHP via Java" API et extrayez-le. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque PHP java/Java.inc (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez "PHP/Java Bridge" dans le dossier ci-dessus avec la commande ci-dessous.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCALE : 8080 >/dev/null 2>&1 &|
|:- |
- Exécutez "example.php" dans le dossier "aspose.cells" pour exécuter l'exemple avec la commande ci-dessous :

|$ php exemple.php|
|:- |
### **Windows:**
- Télécharger[PHP](https://www.php.net/downloads.php)binaire Windows et ajoutez "php.exe" à PATH.
- Installez Oracle JDK (1.7 ou 1.8) pour Windows et configurez la variable d'environnement JAVA_HOME.
- Téléchargez "Aspose.Cells pour PHP via Java" API et extrayez-le. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque PHP java/Java.inc (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez "PHP/Java Bridge" dans le dossier ci-dessus avec la commande ci-dessous. Sélectionnez le port d'écoute http 8080 au démarrage du pont et cliquez sur le bouton OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Exécutez "example.php" dans le dossier "aspose.cells" pour exécuter l'exemple avec la commande ci-dessous :

|> exemple php.php|
|:- |
### **Mac:**
- Installer[PHP](https://www.php.net/downloads.php).
- Installez Oracle JDK (1.7 ou 1.8) pour Mac, configurez la variable d'environnement JAVA_HOME.
- Téléchargez "Aspose.Cells pour PHP via Java" API et extrayez-le. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque PHP java/Java.inc (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez "PHP/Java Bridge" dans le dossier ci-dessus avec la commande ci-dessous. Sélectionnez le port d'écoute http 8080 au démarrage du pont et cliquez sur le bouton OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Exécutez "example.php" dans le dossier "aspose.cells" pour exécuter l'exemple avec la commande ci-dessous :

|$ php exemple.php|
|:- |


