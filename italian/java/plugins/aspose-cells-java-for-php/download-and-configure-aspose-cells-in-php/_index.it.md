---
title: Scarica e Configura Aspose.Cells in PHP
type: docs
weight: 10
url: /it/java/download-and-configure-aspose-cells-in-php/
---

## **Scarica le librerie necessarie**
Scarica le librerie necessarie indicate di seguito. Queste sono necessarie per eseguire gli esempi Aspose.Cells Java in PHP.

- **Aspose:** [Aspose.Cells for Java Componente](https://downloads.aspose.com/cells/java/)
- [Bridge PHP/Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Scarica esempi dai siti di codice sociale**
Le versioni in esecuzione degli esempi disponibili per il download sono disponibili sui siti di codici sociali di seguito menzionati:

-----
### **GitHub**
- **Esempi Aspose.Cells Java in PHP** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Come configurare il codice sorgente sulla piattaforma Linux**
Si prega di seguire questi semplici passaggi per aprire ed estendere il codice sorgente durante l'uso:
## **1. Installa il server Tomcat**
Per installare il server Tomcat, emettere il seguente comando sulla console Linux. Ciò installerà con successo il server Tomcat. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Scarica e Configura PHP/JavaBridge**
Per scaricare i binari di PHP/JavaBridge, emettere il seguente comando sulla console Linux. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Estrai i binari di PHP/JavaBridge emettendo il seguente comando sulla console Linux. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Questo estrarrà il file **JavaBridge.war**. Copialo nella cartella **webapps** di tomcat88 emettendo il seguente comando sulla console Linux. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

Se compare un messaggio di errore, installa **FastCGI** emettendo il seguente comando sulla console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Configura gli esempi Aspose.Cells Java in PHP**
Clonare, esempi PHP emettendo i seguenti comandi all'interno della cartella webapps/JavaBridge.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Come configurare il codice sorgente su Windows Platform**
Si prega di seguire i seguenti passaggi semplici per configurare PHP/Java Bridge su Windows Platform

1. Installa PHP5 e configurarlo come fai normalmente
2. Installa JRE 6 (Java Runtime Environment) se non lo hai già. Puoi controllare questo in C:\Programmi etc. Puoi scaricarlo qui. Sto usando JRE 6 in quanto è compatibile con PHP Java Bridge (PJB).

3. Installa Apache Tomcat 8.0. Puoi scaricarlo qui

4. Scarica [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copia questo file nella directory webapps di tomcat.
(ad esempio: C:\Programmi\Apache Software Foundation\Tomcat 8.0\webapps)

5. Riavvia il servizio tomcat apache.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Copia il file jar di Aspose.Cells Java in C:\Programmi\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clona gli esempi [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) all'interno della cartella C:\Programmi\Apache Software Foundation\Tomcat 8.0\webapps\.

8. Copia la cartella C:\Programmi\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java nella cartella degli esempi di Aspose.Cells Java for PHP.

10. Riavvia il servizio apache tomcat e inizia a utilizzare gli esempi. 
