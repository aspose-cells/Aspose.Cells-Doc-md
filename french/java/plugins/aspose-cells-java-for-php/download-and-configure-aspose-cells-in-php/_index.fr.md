---
title: Télécharger et configurer Aspose.Cells en PHP
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-cells-in-php/
---

## **Télécharger les bibliothèques requises**
Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments nécessaires pour exécuter les exemples Aspose.Cells Java pour PHP.

- **Aspose:** [Composant Aspose.Cells for Java](https://downloads.aspose.com/cells/java/)
- [Pont PHP/Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Téléchargez les exemples des sites de codage social**
Les versions suivantes des exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous:

-----
### **GitHub**
- **Exemples Aspose.Cells Java pour PHP** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Comment configurer le code source sur la plateforme Linux**
Veuillez suivre ces étapes simples pour ouvrir et étendre le code source lors de son utilisation:
## **1. Installer le serveur Tomcat**
Pour installer le serveur Tomcat, saisissez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Télécharger et Configurer PHP/JavaBridge**
Pour télécharger les binaires PHP/JavaBridge, saisissez la commande suivante sur la console Linux. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Décompressez les binaires PHP/JavaBridge en saisissant la commande suivante sur la console Linux. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Cela extraira le fichier **JavaBridge.war**. Copiez-le dans le dossier **webapps** de tomcat8 en lançant la commande suivante dans la console Linux. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Si un message d'erreur apparaît, installez **FastCGI** en lançant la commande suivante dans la console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Configurer Aspose.Cells Java pour les exemples de PHP**
Clonez les exemples de PHP en lançant les commandes suivantes à l'intérieur du dossier webapps/JavaBridge.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Comment configurer le code source sur la plateforme Windows**
Veuillez suivre les étapes simples ci-dessous pour configurer PHP/Java Bridge sur la plateforme Windows

\1. Installez PHP5 et configurez-le comme vous le feriez normalement
\2. Installez JRE 6 (Java Runtime Environment) si vous ne l'avez pas déjà. Vous pouvez vérifier cela dans C:\Program Files etc. Vous pouvez le télécharger ici. J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).

\3. Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici

4. Téléchargez [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copiez ce fichier dans le répertoire webapps de tomcat.
(par exemple: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Redémarrez le service Apache tomcat.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Copiez votre fichier jar Aspose.Cells Java dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\8. Clonez [Aspose.Cells Java pour PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) exemples à l'intérieur de C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ dossier.

\8. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier d'exemples de Aspose.Cells Java pour PHP.

\10. Redémarrez le service apache tomcat et commencez à utiliser les exemples. 
