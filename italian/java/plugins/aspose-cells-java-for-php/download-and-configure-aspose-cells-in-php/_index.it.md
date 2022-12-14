---
title: Scarica e configura Aspose.Cells in PHP
type: docs
weight: 10
url: /it/java/download-and-configure-aspose-cells-in-php/
---
## **Scarica le librerie richieste**
Scarica le librerie richieste menzionate di seguito. Questi sono i requisiti per l'esecuzione di Aspose.Cells Java per esempi PHP.

- **Aspose:** [Aspose.Cells for Java Componente](https://downloads.aspose.com/cells/java/)
- [PHP/Java Ponte](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **Scarica esempi dai siti di codifica sociale**
Le seguenti versioni di esempi in esecuzione sono disponibili per il download sui siti di social coding sotto indicati:

-----
### **Git Hub**
- **Aspose.Cells Java per esempi PHP** 
  - [Aspose.Cells Java per PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Come configurare il codice sorgente su piattaforma Linux**
Si prega di seguire questi semplici passaggi per aprire ed estendere il codice sorgente durante l'utilizzo:
## **1. Installa il server Tomcat**
 Per installare il server Tomcat, emettere il seguente comando sulla console Linux. Questo installerà correttamente il server Tomcat.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. Scarica e configura PHP/JavaBridge**
 Per scaricare i binari PHP/JavaBridge, emettere il seguente comando sulla console Linux.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


 Decomprimi i binari PHP/JavaBridge emettendo il seguente comando sulla console Linux.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


Questo estrarrà**JavaBridge.war**file. Copialo in Tomcat88**webapp** folder emettendo il seguente comando sulla console Linux.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


Copiando, Tomcat8 creerà automaticamente una nuova cartella "**JavaBridge**" in**webapp**. Una volta creata la cartella, assicurati che Tomcat8 sia in esecuzione, quindi controlla<http://localhost:8080/JavaBridge>nel browser, dovrebbe aprire una pagina predefinita di JavaBridge.

 Se viene visualizzato un messaggio di errore, installare**FastCGI**immettendo il seguente comando sulla console Linux.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

Dopo aver installato php5.5 cgi, riavvia il server Tomcat8 e controlla<http://localhost:8080/JavaBridge>nuovamente nel browser.

Se**JAVA_HOME**viene visualizzato l'errore, quindi aprire il file /etc/default/tomcat8 e rimuovere il commento dalla riga che imposta JAVA_HOME. Controlla di nuovo <http://localhost:8080/JavaBridge> nel browser, dovrebbe venire con la pagina degli esempi PHP/JavaBridge.
## **3. Configurare Aspose.Cells Java per esempi PHP**
 Clona, esempi PHP immettendo i seguenti comandi all'interno della cartella webapps/JavaBridge.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Come configurare il codice sorgente sulla piattaforma Windows**
Si prega di seguire i semplici passaggi seguenti per configurare PHP/Java Bridge sulla piattaforma Windows

\1. Installa PHP5 e configura come fai normalmente
\2. Installa JRE 6 (Java Runtime Environment) se non lo hai già. Puoi verificarlo in C:\Program Files ecc. Puoi scaricarlo qui . Sto usando JRE 6 in quanto è compatibile con PHP Java Bridge (PJB).

\3. Installa Apache Tomcat 8.0. Potete scaricarlo qui

 4.Scarica[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copia questo file nella directory webapps di Tomcat.
(es: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Riavvia il servizio Tomcat Apache.

 6.Vai a<http://localhost:8080/JavaBridge/test.php> per verificare se php funziona. Puoi trovare altri esempi lì dentro

7.Copiare il file jar Aspose.Cells Java in C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

 \8. Clone[Aspose.Cells Java per PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) esempi all'interno della cartella C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

\8. Copia la cartella C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java nella cartella Aspose.Cells Java per esempi PHP.

 \10. Riavvia il servizio Apache Tomcat e inizia a utilizzare gli esempi.
