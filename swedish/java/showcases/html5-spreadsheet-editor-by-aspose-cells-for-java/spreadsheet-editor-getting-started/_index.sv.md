---
title: Komma igång med kalkylbladsredigeraren
type: docs
weight: 10
url: /sv/java/spreadsheet-editor-getting-started/
---

Innehållsförteckning

- [Introduktion](#SpreadsheetEditorGettingStarted-Introduction)
- [Systemkrav](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Hämta och installation](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Support](#SpreadsheetEditorGettingStarted-Support)
- [Bidra](#SpreadsheetEditorGettingStarted-Contribute)
- [Licens](#SpreadsheetEditorGettingStarted-License)
### **Introduktion**
Html5 Spreadsheet Editor är en webbapplikation som kan visa och redigera kalkylbladsdokument i en webbläsare. Den stöder Excel, SpreadsheetML, CVS, OpenDocument och många andra format som stöds av Microsoft Excel. Alla grundläggande funktioner inklusive cellredigering, formatering, formelredigering, rad- och kolumnhantering osv. stöds.

![todo:image_alt_text](aowcrc1.png)

HTML5 Spreadsheet Editor använder många funktioner i [Aspose.Cells for Java](https://products.aspose.com/cells/java/) och visar hur man använder dem för att skapa, manipulera och rendera ett kalkylblad i din Java-applikation.

**Funktioner**

- Arbeta med filer 
  - Stödda format
  - Öppna lokala filer
  - Öppna från Dropbox
  - Öppna från URL
  - Skapa ett nytt kalkylblad
  - Exportera till olika format
- Arbeta med ark 
  - Lägga till och ta bort ark
  - Byta namn på ark
  - Växla mellan ark
- Arbeta med rader och kolumner 
  - Lägga till en rad
  - Lägga till en kolumn
  - Ta bort en rad
  - Ta bort en kolumn
  - Kolumnbredd och radhöjd
- Arbeta med celler 
  - Välja en cell
  - Redigera en cell
  - Redigera formel
  - Cellausriktning
  - Rensa cell
  - Lägga till en cell
  - Ta bort en cell
- Arbeta med textformatering 
  - Fet, kursiv, understrykning
  - Teckensnittsstil och storlek
  - Rensa formatering
### **Systemkrav**
**Programvarukrav**

- CDI-stödd Java-applikationsserver
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Maskinvarukrav**

Maskinvarukraven varierar beroende på den Java-applikationsserver vi väljer att distribuera HTML5 Spreadsheet Editor och antalet kalkylblad vi öppnar samtidigt. Följande är en uppskattning som kommer att hjälpa till att initialt konfigurera miljön.

- 2 GHz CPU
- 2 GB RAM
- 500 MB disk
### **Hämta och installation**
HTML5 Spreadsheet Editor är en Java EE-applikation och kan distribueras till vilken Java-applikationsserver webbprofil som helst med CDI-stöd. Den har testats med [Glassfish](https://javaee.github.io/glassfish/).

**Källkod**

Projektkällan finns tillgänglig på [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Vi underhåller även Git-speglingar på följande platser:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Använd en av följande kommandon för att hämta källkoden via kommandoraden:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Bygga med Maven**

Projektbyggprocessen hanteras med Maven. Så du kan förbereda en WAR-fil från kommandoraden utan någon IDE. Använd följande kommando för att generera en WAR för distribution. Dokumentationen för motsvarande applikationsserver kommer att hjälpa dig med hur du distribuerar den genererade WAR-filen och dess beroenden.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**Använda NetBeans**

Det är mycket enkelt att hantera projektet med [NetBeans IDE](https://netbeans.apache.org/). NetBeans är en av de populära IDE:erna bland Java-utvecklare och sponsras av Oracle.

- Hämta projektkällkoden.
- Öppna projektet i NetBeans IDE.
- Klicka på ***Kör***-knappen på verktygsfältet.
- Välj ***Glassfish***-server som applikationsserver.

**Använda Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) erbjuder officiell integration för att importera Maven-projekt som kallas [M2Eclipse](http://www.eclipse.org/m2e/):

1. Installera M2Eclipse i din Eclipse IDE. installationsproceduren beskrivs på deras webbplats.
1. Hämta projektkällkoden.
1. Öppna ***Importera***-dialogrutan från Arkiv-menyn.
1. Välj ***Maven-projekt*** från importdialogrutan.
1. Klicka på ***Nästa***.
1. Klicka på ***Bläddra*** för att välja platsen för källkoden.
1. Välj ***pom.xml*** från listan nedan.
1. Klicka på ***Avsluta***.

Eclipse IDE bör importera och ladda projektet.
### **Support**
**Felrapport**

För att skicka in en felrapport, skapa en ny fråga på [GitHubs projektsida](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) och lägg till etiketten ***fel***.

**Funktionsförfrågan**

Vi uppskattar mycket dina åsikter och de funktioner du begär. För att begära en ny funktion eller förbättring i en befintlig, skapa en ny fråga på [GitHubs projektsida](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) och lägg till etiketten ***förbättring***.

**Frågor och Hjälp**

Du kan ställa alla typer av frågor relaterade till HTML5 Spreadsheet Editor med [GitHubs fråga](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). Skapa bara en ny fråga och lägg till etiketten ***fråga***.

**Aspose.Cells for Java Forum**

Aspose-produktforum ger fullt stöd för både test- och betalande kunder. Experter sitter 24/7 för att ge hjälp och svara på frågor. Besök [produkforum här](https://forum.aspose.com/c/cells/9).

**Aspose Bloggar**

Ta kontakt med oss och håll dig uppdaterad med de senaste nyheterna om våra produkter och erbjudanden. Prenumerera på [vår blogg här](http://blog.aspose.com).
### **Bidra**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5 Spreadsheet Editor är ett öppet projekt som tillåter maximala alternativ för alla att bidra till projektet.

**Källkod**

Projektkällkoden finns tillgänglig på [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Vi håller också Git-speglar på följande platser:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Pull-förfrågningar**

Om du vill bidra med källkod till projektet, skicka bara en pull-förfrågan via Github. Läs mer information i GitHubs artikel om [Skapa en pull-förfrågan](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licens**
**MIT-licens**

Vi använder en av de mest liberala öppna källkodstillstånden för minsta ansvar för bidragsgivare. HTML5 Spreadsheet Editor släpps under [MIT-licensen](https://opensource.org/licenses/mit-license.php).

**Aspose-licens**

Produkten fungerar utan Aspose-licens, [med begränsningar](/cells/sv/java/licensing/). För att ta bort begränsningar kan du skaffa en [gratis tillfällig licens](https://purchase.aspose.com/temporary-license) eller [köpa full licens](https://purchase.aspose.com/buy).

Som standard kommer editorn att försöka ladda filen **Aspose.Total.Java.lic** från katalogen **src/main/resources/com/aspose/spreadsheeteditor**. Kopiera bara licensfilen till denna katalog. Det standardbeteendet kan ändras genom att redigera klassen **AsposeLicense**.
{{< app/cells/assistant language="java" >}}
