---
title: Introduktion av GridWeb
type: docs
weight: 10
url: /sv/java/introduction-of-gridweb/
---
## **Grundläggande i GridWeb**
Aspose.Cells.GridWeb är en GUI-baserad webbkontroll som kan bäddas in i JSP-webbsidor eller vilken HTML-sida som helst i java-server. 
{{% alert color="primary" %}} 

Det är enkelt och enkelt att använda.

Det hjälper dig att snabbt bygga en online webbredigerare för kalkylbladsfil.

Det stöder också import och export av alla typer av kalkylbladsformatfiler som är 100% kompatibla med MS Excel-filer.

## **Aspose.Cells.GridWeb - Demos**
{{% alert color="primary" %}} 

För att snabbt komma igång, tillhandahåller vi ett antal kodexempel och demo som visar hur man använder Aspose.Cells.GridWeb API.

Vänligen ladda ner demo från nedanstående länk:
[Aspose.Cells.GridWeb Demos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Hur man kör Aspose.Cells for GridWeb Java Demos**
{{% alert color="primary" %}} 

Aspose.Cells for GridWeb Java-demon är enkla att köra. Du behöver bara distribuera ** gridwebdemo.war ** på din webbserver. Vänligen ladda ner demo från denna [länk](https://forum.aspose.com/uploads/discourse_instance3/22292).

Den här artikeln beskriver hur man kör Aspose.Cells for GridWeb Java Demos i Apache Tomcat Server.

{{% /alert %}} 
### **Steg för steg-guide för att köra GridWeb Java Demos**
1. Packa upp ** apache-tomcat-7.0.52.zip ** i valfri katalog t.ex. C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



Följande ögonblicksbild visar de extraherade katalogerna och filerna i Apache Tomcat-servern 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Du kan också behöva ställa in miljövariabeln **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Öppna filen **tomcat-users.xml**. 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Lägg till den här användaren:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Här är användarnamnet tomcat och lösenordet är hemligt** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Kör **startup.bat** filen.
   Det kommer att köra Apache Tomcat Server. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Tomcat server körs i en kommandofönster** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Öppna nu webbläsaren och skriv **localhost:8080**.
   Apache Tomcats webbsida visas. 

   **Apache Tomcats webbsida** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Klicka på **Manager App** och skriv användarnamn och lösenord. (Som ovan: tomcat, hemligt) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Bläddra ned till avsnittet **WAR-fil att distribuera** och bläddra igenom **gridwebdemo.war** filen.
1. Klicka på **Deploy**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Bläddra **gridwebdemo.war** filen. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Klicka på **Deploy**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. När den har distribuerats, klicka på **/gridwebdemo** och starta demo. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


GridWeb Demo-sidan visas. 

**GridWeb Demo-sidan** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Klicka på vilket demo som helst och kör det. 

   **Skapar innehållsdemo körs** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Arbetsbladens demo körs** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar och CommandButton demo körs** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **Webbläsares förmågor och Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb är en GUI-baserad webbkontroll som kan bäddas in i JSP-webbsidor som andra webbkontroller. Det viktigaste med webbkontrollen är att tillhandahålla stöd för olika webbläsare. Aspose.Cells.GridWeb tillhandahåller stöd för olika webbläsare.
### **Jämförelse**
Aspose.Cells.GridWeb stöds fullt ut i Microsofts Internet Explorer (IE). Dock har den mindre begränsningar i andra webbläsare. Denna artikel ger en detaljerad jämförelse av vilka funktioner som stöds av olika webbläsare.

|**Klientens sidofunktioner**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Cellens snabbmeny|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Klientens sidvalidering|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Dubbelklickshändelse|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList ( *ComboBox-läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList ( *Popup Meny-läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formel inmatning/rediger|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Frys eller Avfrys Rader/Kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlänkar ( *CellKommando Läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Hyperlänkar ( *URL Läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sammanfoga eller Avsammanfoga Cellar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Kopiera/Klistra in Flera Cellar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Inmatning/redigering av Flera Cellar, enda efteranskickning|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Nummerformat|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Arkblad Sidnumrering|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Skrivskyddade Cellar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Skrivskyddade Rader/Kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Data Validering med Reguljära Uttryck|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ändra Kolumnbredd|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ändra Radhöjd|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Infoga/Ta bort Rader & Kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Rulla innehåll|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Rulla Arkflikar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ange cellers ramar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ange fontinställningar för celler|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
