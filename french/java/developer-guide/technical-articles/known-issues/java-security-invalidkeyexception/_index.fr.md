---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /fr/java/java-security-invalidkeyexception/
---

## **Résumé**
Par défaut, l'AES prend en charge une clé de 128 bits. Si vous prévoyez d'utiliser une clé de 192 bits ou de 256 bits, le compilateur Java affichera une exception de taille de clé illégale. Ce n'est pas dû à un bug de l'API Aspose.Cells, mais plutôt à la fonctionnalité limitée de JDK/JRE lui-même. Les fichiers de stratégie par défaut de JDK/JRE sont limités en raison de restrictions à l'importation dans certains pays. Les utilisateurs doivent obtenir les fichiers de stratégie "Force illimitée" et les installer dans leur JRE pour utiliser la fonctionnalité de cryptographie avancée pour le chiffrement/déchiffrement.
## **Symptômes**
Vous pouvez recevoir l'exception java.security.InvalidKeyException: Taille de clé illégale ou paramètres par défaut ou java.security.InvalidKeyException: Taille de clé illégale lors du chargement d'une feuille de calcul protégée. 
## **Solution**
La solution est en fait très simple comme indiqué ci-dessous.

1. Téléchargez les fichiers de politique de juridiction de force illimitée d'extension de cryptographie Java (JCE).
1. Extrayez les fichiers JAR de l'archive téléchargée et placez-les dans le répertoire ${java.home}/jre/lib/security/.
1. Relancez le programme.
## **Liens de téléchargement**
Veuillez utiliser le lien de téléchargement correspondant à votre version de JDK/JRE.

- [Fichiers de politique de juridiction de force illimitée d'extension de cryptographie Java 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Fichiers de politique de juridiction de force illimitée d'extension de cryptographie Java 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Fichiers de politique de juridiction de force illimitée d'extension de cryptographie Java 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
