---
title: Kalkylarksredigerare Komma igång
type: docs
weight: 10
url: /sv/java/spreadsheet-editor-getting-started/
---
**Innehållsförteckning**

- [Introduktion](#SpreadsheetEditorGettingStarted-Introduction)
- [Systemkrav](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Ladda ner och installation](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Stöd](#SpreadsheetEditorGettingStarted-Support)
- [Bidra](#SpreadsheetEditorGettingStarted-Contribute)
- [Licens](#SpreadsheetEditorGettingStarted-License)
### **Introduktion**
Html5 Spreadsheet Editor är en webbapplikation som kan visa och redigera kalkylarksdokument i en webbläsare. Den stöder Excel, SpreadsheetML, CVS, OpenDocument och många andra format som stöds av Microsoft Excel. Alla grundläggande funktioner inklusive cellredigering, formatering, formelredigering, rad- och kolumnhantering etc. stöds.

![todo:image_alt_text](aowcrc1.png)

 HTML5 Spreadsheet Editor använder många funktioner i[Aspose.Cells för Java](https://products.aspose.com/cells/java/) och visar hur du använder dem för att skapa, manipulera och rendera ett kalkylblad i din Java-applikation.

**Funktioner**

-  Arbeta med filer
 - Format som stöds
 - Öppna lokala filer
 - Öppna från Dropbox
 - Öppna från URL
 - Skapa ett nytt kalkylblad
 - Exportera till olika format
-  Arbeta med Sheets
 - Lägg till och ta bort ark
 - Byt namn på ark
 - Växla mellan ark
-  Arbeta med rader och kolumner
 - Lägg till en rad
 - Lägg till en kolumn
 - Ta bort en rad
 Ta bort en kolumn
 - Kolumnbredd och radhöjd
-  Arbetar med Cells
 - Välja en cell
 - Redigera en cell
 - Redigera formel
 - Cell uppriktning
 - Rensa Cell
 - Lägg till en cell
 - Ta bort en cell
-  Arbeta med textformatering
 - Fet, kursivt, understruket
 - Teckensnittsstil och storlek
 - Rensa formatering
### **Systemkrav**
**Programvarukrav**

- CDI-stödd Java-applikationsserver
- [Aspose.Cells för Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Hårdvarukrav**

Hårdvarukraven varierar beroende på vilken Java-applikationsserver vi väljer att distribuera HTML5 Spreadsheet Editor och antalet kalkylblad vi öppnar samtidigt. Följande är en uppskattning som kommer att hjälpa till att initialt ställa in miljön.

- 2 GHz CPU
- 2 GB RAM
- 500 MB disk
### **Ladda ner och installation**
 HTML5 Spreadsheet Editor är en Java EE-applikation och kan distribueras till valfri Java-applikationsserverwebbprofil med CDI-stöd. Den har testats med[Glasfisk](https://javaee.github.io/glassfish/).

**Källkod**

Projektkällan finns tillgänglig på[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Vi underhåller även Git-speglar på följande webbplatser:

- [Bit hink](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google-kod](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Använd ett av följande kommandon för att ladda ner källkoden via kommandoraden:

**Github**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bit hink**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google-kod**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Bygg med Maven**

Projektkonstruktionsprocessen hanteras med Maven. Så du kan förbereda en WAR-fil från kommandoraden utan någon IDE. Använd följande kommando för att generera en WAR för distribution. Dokumentationen för motsvarande applikationsserver hjälper dig att distribuera den genererade WAR och dess beroenden.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Använder NetBeans**

 Det är väldigt enkelt att hantera projektet med hjälp av[NetBeans IDE](https://netbeans.apache.org/). NetBeans är en av de populära IDEerna bland Java-utvecklare och sponsras av Oracle.

- Ladda ner projektets källkod.
- Öppna projektet i NetBeans IDE.
-  Klick***Springa*** knappen i verktygsfältet.
-  Välj***Glasfisk*** server som applikationsserver.

**Använder Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) ger officiell integration för att importera Maven-projekt som kallas[M2Eclipse](http://www.eclipse.org/m2e/):

1. Installera M2Eclipse i din Eclipse IDE. Installationsproceduren beskrivs på deras hemsida.
1. Ladda ner projektets källkod.
1.  Öppna***Importera*** dialogrutan från Arkiv-menyn.
1.  Välj***Maven-projektet*** från importdialogrutan.
1.  Klick***Nästa***.
1.  Klick***Bläddra*** för att välja platsen för källkoden.
1.  Välj***pom.xml*** från listan nedan.
1.  Klick***Avsluta***.

Eclipse IDE bör importera och ladda projektet.
### **Stöd**
**Buggrapport**

 För att skicka en felrapport, skapa ett nytt problem på[Github projektsida](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) och applicera etiketten***insekt***.

**Funktionsbegäran**

 Vi uppskattar mycket din feedback och de funktioner du efterfrågar. För att begära en ny funktion eller förbättring av befintliga, skapa ett nytt nummer på[Github projektsida](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) och applicera etiketten***förbättring***.

**Frågor och hjälp**

 Du kan ställa alla typer av frågor relaterade till HTML5 Spreadsheet Editor med hjälp av[Github problem](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Skapa bara ett nytt nummer och tillämpa***fråga*** märka.

**Aspose.Cells för Java-forum**

 Aspose produktforum ger full support för både test- och betalkunder. Experter sitter 24/7 för att ge hjälp och svara på frågor. Besök[produktforum här](https://forum.aspose.com/c/cells/9).

**Aspose Bloggar**

 Kontakta oss och håll dig uppdaterad med de senaste nyheterna om våra produkter och erbjudanden. Prenumerera på[vår blogg här](http://blog.aspose.com).
### **Bidra**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Kalkylblad_Redaktör_förbi_Aspose.Cells_för_Java)


HTML5 Spreadsheet Editor är ett projekt med öppen källkod som ger maximala möjligheter för alla att bidra till projektet.

**Källkod**

Projektkällan finns tillgänglig på[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Vi underhåller även Git-speglar på följande webbplatser:

- [Bit hink](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Dra förfrågningar**

 För att bidra med källkod till projektet skickar du bara en pull-förfrågan via Github. Läs mer information i Githubs artikel om[Skapa en pull-begäran](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licens**
**MIT-licens**

 Vi använder en av de mest liberala licenserna för öppen källkod för minimiskulder på bidragsgivare. HTML5 Spreadsheet Editor släpps under[MIT-licens](https://opensource.org/licenses/mit-license.php).

**Aspose Licens**

 Produkten fungerar utan Aspose licens,[med begränsningar](/cells/sv/java/licensing/) . För att ta bort begränsningar kan du skaffa en[gratis tillfällig licens](https://purchase.aspose.com/temporary-license) eller[köpa full licens](https://purchase.aspose.com/buy).

Som standard kommer redigeraren att försöka ladda**Aspose.Total.Java.lic** fil från**src/main/resources/com/aspose/spreadsheeteditor** katalog. Kopiera bara licensfilen till den här katalogen. Standardbeteendet kan ändras genom att redigera**AsposeLicens** klass.
