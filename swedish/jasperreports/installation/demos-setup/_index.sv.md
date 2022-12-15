---
title: Demoinställningar
type: docs
weight: 40
url: /sv/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports innehåller ett antal demoprojekt som hjälper dig att komma igång med att exportera rapporter till Microsoft Excel-dokumentformat från din applikation.

Demos som tillhandahålls med Aspose.Cells for JasperReports är standarddemos från JasperReports modifierade för att visa användningen av de nya exportörerna.

{{% /alert %}}

För att köra Aspose.Cells for JasperReports demos, utför följande steg:

1.  Ladda ner JasperReports (t.ex<https://sourceforge.net/projects/jasperreports/files/archive/>). Se till att ladda ner hela det arkiverade projektet med källkoden och demos, inte bara en enda JAR.
1. Packa upp det arkiverade projektet till någon plats på din hårddisk, till exempel C:\.
1.  Kopiera alla demo-mappar från mappen \demo**Aspose.Cells.JasperReports.zip** till**\<InstallDir>\demo\samples**, var "\<InstallDir>" är platsen du har packat upp JasperReports till. Det här steget krävs eftersom demobyggande skript förlitar sig på JasperReports mappstruktur, annars måste du ändra byggskript.
1.  Kopiera**aspose.cells.jasperreports.jar** från mappen \lib i Aspose.Cells.JasperReports.zip till**\<InstallDir>\lib**.
1.  Förbered Ant Build Tool och Ivy Dependency Manager, se**\<InstallDir>\readme.txt**.
1.  Ändra**build.xml** på**\<InstallDir>\demo\samples**, lägg till aspose.cells.jasperreports.jar i klasssökvägen:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1.  Ändra den aktuella katalogen till**\<InstallDir>\demo\hsqldb** och kör följande kommandorad:
   **ant runServer**
1.  Ändra den aktuella katalogen till en av Aspose.Cells for JasperReports demos, till exempel**\<InstallDir>\demo\samples\ac.charts** och kör följande kommandon på kommandoraden:
   **myrtest** - att producera rapportfiler med hjälp av Aspose XLS exporter.
1.  Öppna ett av de resulterande dokumenten för att se till exempel**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** i Microsoft Excel eller annan applikation.
