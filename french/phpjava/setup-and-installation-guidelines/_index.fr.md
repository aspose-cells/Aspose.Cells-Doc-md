---
title: Directives de configuration et d installation
type: docs
weight: 20
url: /fr/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "configuration d Aspose.Cells pour PHP via Java et directives d installation"
---



## **Configuration requise**
Aspose.Cells pour PHP via Java est une API indépendante de la plateforme et peut être utilisée sur n'importe quelle plateforme (Windows, Linux, MacOS, etc.) où PHP 7 ou des versions ultérieures sont installées. La machine doit avoir Oracle JDK 7 ou des versions ultérieures avant de procéder à l'installation.
## **Installation et Utilisation**
Aspose.Cells pour PHP via Java est distribué sous forme d'archive ZIP.

Pour configurer l'environnement, installer et utiliser Aspose.Cells pour PHP via Java, suivez les instructions suivantes :
### **Linux:**
- Téléchargez la source de PHP (https://www.php.net/downloads.php) et installez-la. Ou utilisez la commande "sudo apt install php-xxx" pour installer le binaire PHP.
- Installez Oracle JDK (1.7 ou 1.8) pour Linux, configurez la variable d'environnement JAVA_HOME.
- Téléchargez/obtenez l'API "Aspose.Cells pour PHP via Java" et extrayez-la. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire de PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque java/Java.inc PHP (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez "PHP/Java Bridge" dans le dossier ci-dessus avec la commande ci-dessous.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Exécutez "example.php" dans le dossier “aspose.cells” pour exécuter l'exemple avec la commande ci-dessous :

|$ php example.php|
| :- |
### **Windows:**
- Téléchargez le binaire Windows de PHP (https://www.php.net/downloads.php) et ajoutez "php.exe" au PATH.
- Installez Oracle JDK (1.7 ou 1.8) pour Windows et configurez la variable d'environnement JAVA_HOME.
- Téléchargez l'API "Aspose.Cells for PHP via Java" et extrayez-la. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire de PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque java/Java.inc PHP (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez le “PHP/Java Bridge” dans le dossier ci-dessus avec la commande ci-dessous. Sélectionnez le port d'écoute http 8080 lorsque le bridge démarre et cliquez sur le bouton OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Exécutez "example.php" dans le dossier “aspose.cells” pour exécuter l'exemple avec la commande ci-dessous :

|> php example.php|
| :- |
### **Mac:**
- Installez [PHP](https://www.php.net/downloads.php).
- Installez Oracle JDK (1.7 ou 1.8) pour Mac, configurez la variable d'environnement JAVA_HOME.
- Téléchargez l'API "Aspose.Cells for PHP via Java" et extrayez-la. Il y aura un dossier nommé "aspose.cells".
- Téléchargez le binaire de PHP/Java Bridge (JavaBridge.jar) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-le dans le dossier "aspose.cells".
- Téléchargez la bibliothèque java/Java.inc PHP (Java.inc) depuis http://php-java-bridge.sourceforge.net/pjb/download.php et enregistrez-la dans le dossier "aspose.cells".
- Exécutez le “PHP/Java Bridge” dans le dossier ci-dessus avec la commande ci-dessous. Sélectionnez le port d'écoute http 8080 lorsque le bridge démarre et cliquez sur le bouton OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Exécutez "example.php" dans le dossier “aspose.cells” pour exécuter l'exemple avec la commande ci-dessous :

|$ php example.php|
| :- |


