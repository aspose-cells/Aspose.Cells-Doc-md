---
title: Introduktion av GridWeb
type: docs
weight: 10
url: /sv/java/introduction-of-gridweb/
---
## **Hur man kör Aspose.Cells för GridWeb Java Demos**
{{% alert color="primary" %}} 

 Aspose.Cells för GridWeb Java-demos är lätta att köra. Du behöver bara distribuera**gridwebdemo.war** i din webbserver. Ladda ner demos från denna[länk](https://forum.aspose.com/uploads/discourse_instance3/22292).

Den här artikeln beskriver hur du kör Aspose.Cells för GridWeb Java Demos i Apache Tomcat Server.

{{% /alert %}} 
### **Steg för steg guide för att köra GridWeb Java Demos**
1.  Extrahera**apache-tomcat-7.0.52.zip** i vilken katalog som helst, t.ex. C:\Tomcat

![todo:image_alt_text](introduction-of-gridweb_1.png)



 Följande ögonblicksbild visar de extraherade katalogerna och filerna för Apache Tomcat-servern

![todo:image_alt_text](introduction-of-gridweb_2.png)



 Du kan också behöva ställa in miljövariabeln**CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1.  Öppna**tomcat-users.xml** fil.

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Lägg till denna användare:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Här är användarnamnet tomcat och lösenordet är hemligt** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1.  Springa det**startup.bat** fil.
 Den kommer att köra Apache Tomcat Server.

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Tomcat-server som körs i ett kommandofönster** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1.  Öppna nu webbläsaren och skriv**lokal värd: 8080**.
 Webbsidan för Apache Tomcat visas.

   **Apache Tomcat webbsida** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1.  Klick**Manager-app**och skriv användarnamn och lösenord. (Som ovan: Tomcat, hemlig)

![todo:image_alt_text](introduction-of-gridweb_9.png)

1.  Scrolla ner till avsnittet**WAR-fil att distribuera** och bläddra i**gridwebdemo.war** fil.
1.  Klick**Distribuera**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1.  Bläddra**gridwebdemo.war** fil.

![todo:image_alt_text](introduction-of-gridweb_11.png)

1.  Klick**Distribuera**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1.  Klicka på när den har distribuerats**/gridwebdemo** och börja köra demos.

![todo:image_alt_text](introduction-of-gridweb_13.png)


 GridWeb-demosidan visas.

**GridWeb-demosidan** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1.  Klicka på valfri demo och kör den.

   **Skapar innehållsdemo körs** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Demo av arbetsblad körs** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar och CommandButton-demo körs** 

![todo:image_alt_text](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - Demos**
{{% alert color="primary" %}} 

För att du ska komma igång snabbt tillhandahåller vi ett antal kodexempel och demos som visar hur du använder Aspose.Cells.GridWeb API.

Ladda ner demos från länken nedan:
[Aspose.Cells.GridWeb Demos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Webbläsarfunktioner och Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb är en GUI-baserad webbkontroll som kan bäddas in i JSP-webbsidor som andra webbkontroller. Det viktigaste med webbkontroll är att tillhandahålla stöd över webbläsare. Aspose.Cells.GridWeb tillhandahåller stöd för flera webbläsare.
### **Jämförelse**
Aspose.Cells.GridWeb stöds fullt ut på Microsofts Internet Explorer (IE). På andra webbläsare har den dock mindre begränsningar. Det här avsnittet ger en detaljerad jämförelse av vilka funktioner som stöds av olika webbläsare.

|**Funktioner på klientsidan**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
|:- |:- |:- |:- |:- |
|Snabbmeny för Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validering på klientsidan|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Dubbelklicka på händelse|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| DropDown List (*ComboBox-läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| DropDown List (*Popup-menyläge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formelinmatning/redigering|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Frys eller lås upp rader/kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlänkar (*CellCommand-läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Hyperlänkar (*URL-läge* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sammanfoga eller ta bort sammanfogningen Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Flera Cells Kopiera/klistra in|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Flera Cells Inmatning/redigera, enkel återsändning|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Nummerformat|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Bladsökning|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Skrivskyddat Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Skrivskyddade rader/kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Datavalidering med hjälp av reguljära uttryck|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ändra storlek på kolumnbredd|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ändra storlek på radhöjd|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Infoga/ta bort rader och kolumner|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Bläddra innehåll|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Rulla arkflikar|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ställ in gränser för Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ställ in teckensnittsinställningar för Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} En cells snabbmeny kan endast aktiveras genom att klicka på menyknappen på klientsidan.
