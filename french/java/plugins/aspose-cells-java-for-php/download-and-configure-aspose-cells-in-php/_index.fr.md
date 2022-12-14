---
title: Téléchargez et configurez Aspose.Cells en PHP
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-cells-in-php/
---
## **Télécharger les bibliothèques requises**
Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments requis pour exécuter Aspose.Cells Java pour les exemples PHP.

- **Aspose:** [Aspose.Cells for Java Composant](https://downloads.aspose.com/cells/java/)
- [Pont PHP/Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Télécharger des exemples à partir de sites de codage social**
Les versions suivantes des exemples en cours d'exécution sont disponibles au téléchargement sur les sites de codage social mentionnés ci-dessous :

-----
### **GitHub**
- **Aspose.Cells Java pour les exemples PHP** 
  - [Aspose.Cells Java pour PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Comment configurer le code source sur la plate-forme Linux**
Veuillez suivre ces étapes simples afin d'ouvrir et d'étendre le code source lors de l'utilisation :
## **1. Installez le serveur Tomcat**
 Pour installer le serveur Tomcat, exécutez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Téléchargez et configurez PHP/JavaBridge**
 Pour télécharger les binaires PHP/JavaBridge, lancez la commande suivante sur la console Linux.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


 Décompressez les fichiers binaires PHP/JavaBridge en exécutant la commande suivante sur la console Linux.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Cela va extraire**JavaBridge.war**dossier. Copiez-le dans tomcat88**applications Web** dossier en exécutant la commande suivante sur la console Linux.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


En copiant, tomcat8 créera automatiquement un nouveau dossier "**JavaBridge**" dans**applications Web**. Une fois le dossier créé, assurez-vous que votre tomcat8 est en cours d'exécution, puis vérifiez<http://localhost:8080/JavaBridge>dans le navigateur, il devrait ouvrir une page par défaut de JavaBridge.

 Si un message d'erreur apparaît, installez**FastCGI**en exécutant la commande suivante sur la console Linux.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

Après avoir installé php5.5 cgi, redémarrez le serveur tomcat8 et vérifiez<http://localhost:8080/JavaBridge>à nouveau dans le navigateur.

Si**JAVA_HOME**s'affiche, puis ouvrez le fichier /etc/default/tomcat8 et décommentez la ligne qui définit le JAVA_HOME. Vérifiez à nouveau <http://localhost:8080/JavaBridge> dans le navigateur, il devrait être accompagné de la page Exemples PHP/JavaBridge.
## **3. Configurez Aspose.Cells Java pour les exemples PHP**
 Clonez des exemples PHP en exécutant les commandes suivantes dans le dossier webapps/JavaBridge.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Comment configurer le code source sur la plate-forme Windows**
Veuillez suivre les étapes simples ci-dessous pour configurer le pont PHP/Java sur la plate-forme Windows

\1. Installez PHP5 et configurez comme vous le faites normalement
\2. Installez JRE 6 (environnement d'exécution Java) si vous ne l'avez pas déjà. Vous pouvez le vérifier dans C:\Program Files, etc. Vous pouvez le télécharger ici . J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).

\3. Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici

 4.Télécharger[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copiez ce fichier dans le répertoire tomcat webapps.
(ex : C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Redémarrez le service Tomcat Apache.

 6.Allez à<http://localhost:8080/JavaBridge/test.php> pour vérifier si php fonctionne. Vous pouvez y trouver d'autres exemples

7.Copiez votre fichier jar Aspose.Cells Java dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8. Cloner[Aspose.Cells Java pour PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) exemples dans le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier Aspose.Cells Java pour les exemples PHP.

 \dix. Redémarrez le service Apache Tomcat et commencez à utiliser des exemples.
