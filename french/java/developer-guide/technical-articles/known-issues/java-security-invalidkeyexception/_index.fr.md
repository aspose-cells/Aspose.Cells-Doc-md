---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /fr/java/java-security-invalidkeyexception/
---
## **Sommaire**
Par défaut, l'AES prend en charge une clé de 128 bits, si vous prévoyez d'utiliser une clé de 192 ou 256 bits, le compilateur Java lancera une exception de taille de clé illégale. Cela n'est pas dû à un bogue de Aspose.Cells API, mais plutôt à la fonctionnalité limitée de JDK/JRE lui-même. Les fichiers de stratégie par défaut de JDK/JRE sont paralysés en raison des restrictions d'importation dans certains pays. Les utilisateurs doivent obtenir les fichiers de stratégie "Unlimited Strength" et les installer dans leur JRE pour utiliser la fonctionnalité de cryptographie avancée pour le chiffrement/déchiffrement.
## **Les symptômes**
 Vous pouvez obtenir java.security.InvalidKeyException : taille de clé illégale ou paramètres par défaut ou java.security.InvalidKeyException : taille de clé illégale lors du chargement d'une feuille de calcul protégée.
## **La solution**
La solution est en fait très simple comme détaillé ci-dessous.

1. Téléchargez les fichiers de stratégie de juridiction de force illimitée Java Cryptography Extension (JCE).
1. Extrayez les fichiers JAR de l'archive téléchargée et placez-les dans le répertoire ${java.home}/jre/lib/security/.
1. Relancez le programme.
## **Liens de téléchargement**
Veuillez utiliser le lien de téléchargement correspondant à votre version JDK/JRE.

- [Java Extension de chiffrement (JCE) Fichiers de politique de juridiction à force illimitée 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Extension de chiffrement (JCE) Fichiers de politique de juridiction à force illimitée 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Extension de cryptographie (JCE) Fichiers de politique de juridiction à force illimitée 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
