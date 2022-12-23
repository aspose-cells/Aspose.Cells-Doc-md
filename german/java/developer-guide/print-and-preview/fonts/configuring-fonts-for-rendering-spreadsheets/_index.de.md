---
title: Konfigurieren von Schriftarten zum Rendern von Tabellenkalkulationen
type: docs
weight: 10
url: /de/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells-APIs bieten die Möglichkeit, die Tabellenkalkulationen in Bildformaten zu rendern und sie in die Formate PDF und XPS zu konvertieren. Um die Konvertierungstreue zu maximieren, müssen die in der Tabelle verwendeten Schriftarten im Standardverzeichnis für Schriftarten des Betriebssystems verfügbar sein. Falls die erforderlichen Schriftarten nicht vorhanden sind, versuchen die Aspose.Cells-APIs, die erforderlichen Schriftarten durch die verfügbaren zu ersetzen.

## **Auswahl an Schriftarten**

Unten ist der Prozess, dem Aspose.Cells-APIs hinter den Kulissen folgen.

1. Der API versucht, die Schriftarten im Dateisystem zu finden, die genau mit dem in der Tabelle verwendeten Schriftartnamen übereinstimmen.
1.  Wenn API die Schriftarten mit genau demselben Namen nicht finden kann, versucht es, die unter der Arbeitsmappe angegebene Standardschriftart zu verwenden[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) Eigentum.
1.  Wenn API die unter der Arbeitsmappe definierte Schriftart nicht finden kann[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) -Eigenschaft versucht es, die unter angegebene Schriftart zu verwenden[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) oder[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) Eigentum.
1.  Wenn API die unter definierte Schriftart nicht finden kann[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) oder[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) -Eigenschaft versucht es, die unter angegebene Schriftart zu verwenden[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) Eigentum.
1.  Wenn API die unter definierte Schriftart nicht finden kann[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) -Eigenschaft versucht es, die am besten geeigneten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Wenn schließlich API keine Schriftarten im Dateisystem finden kann, wird die Tabelle mit Arial gerendert.

{{% alert color="primary" %}}

 Die Aspose.Cells-APIs scannen immer das Standardschriftverzeichnis des Betriebssystems mit einer Ausnahme, das heißt; wenn JVM argumentiert**-DAspose.Cells.FontDirExc="YourFontDir"**eingestellt sind. In diesem Fall überspringen die Aspose.Cells-APIs das Scannen des Standardverzeichnisses für Schriftarten des Betriebssystems und durchsuchen nur den Pfad, der in den oben genannten JVM-Argumenten angegeben ist.

{{% /alert %}}

## **Legen Sie benutzerdefinierte Schriftordner fest**

 Aspose.Cells APIs durchsuchen das Standardverzeichnis für Schriftarten des Betriebssystems nach den erforderlichen Schriftarten. Falls die erforderlichen Schriftarten nicht im Schriftartenverzeichnis des Systems verfügbar sind, durchsuchen die APIs die benutzerdefinierten (benutzerdefinierten) Verzeichnisse. Das[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)Die Klasse hat eine Reihe von Möglichkeiten zum Festlegen benutzerdefinierter Schriftartenverzeichnisse gezeigt, wie unten beschrieben.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): Diese Methode ist nützlich, wenn sich die Schriftarten in mehreren Ordnern befinden und der Benutzer alle Ordner separat festlegen möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Dieser Mechanismus ist nützlich, wenn der Benutzer Schriftarten aus mehreren Ordnern oder eine einzelne Schriftartdatei oder Schriftartdaten aus einem Array von Bytes laden möchte.

{{% alert color="primary" %}}

 Beide[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) )-Methoden akzeptieren einen zweiten Parameter vom Typ Boolean. Vorbeigehen**wahr**Der zweite Parameter weist die Aspose.Cells-APIs an, die Unterordner nach den Schriftartdateien zu durchsuchen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Bitte verwenden Sie zu Beginn der Bewerbung eine der oben genannten Methoden, d.h. bevor andere Objekte von Aspose.Cells-APIs aufgerufen werden.

{{% /alert %}} {{% alert color="primary" %}}

Wenn mehr als eine der oben genannten Methoden zum Festlegen der Schriftartquellen verwendet wird, werden nur die letzten Einstellungen wirksam.

{{% /alert %}}

## **Font-Ersetzungsmechanismus**

Aspose.Cells-APIs bieten auch die Möglichkeit, die Ersatzschriftart für Wiedergabezwecke anzugeben. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Computer, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste mit Schriftartnamen als Alternative zur ursprünglich erforderlichen Schriftart bereitstellen. Um dies zu erreichen, haben die Aspose.Cells-APIs die Methode FontConfigs.setFontSubstitutes verfügbar gemacht, die zwei Parameter akzeptiert. Der erste Parameter ist vom Typ**Schnur** , das sollte der Name der Schriftart sein, die ersetzt werden muss. Der zweite Parameter ist ein Array vom Typ**Schnur**. Benutzer können eine Liste mit Schriftartnamen als Ersatz für die ursprüngliche Schriftart (angegeben im ersten Parameter) bereitstellen.

Hier ist ein einfaches Nutzungsszenario.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Informationsbeschaffung**

Zusätzlich zu den oben erwähnten Methoden haben die Aspose.Cells-APIs auch Mittel bereitgestellt, um Informationen darüber zu sammeln, welche Quellen und Ersetzungen eingestellt wurden.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): Diese Methode gibt ein Array vom Typ zurück[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)enthält die Liste der angegebenen Schriftartquellen. Falls keine Quellen eingestellt wurden, wird die[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources())-Methode gibt ein leeres Array zurück.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): Diese Methode akzeptiert einen Parameter vom Typ**Schnur** Ermöglicht die Angabe des Schriftartnamens, für den die Ersetzung festgelegt wurde. Falls für den angegebenen Schriftartnamen keine Ersetzung festgelegt wurde, dann die[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String))-Methode gibt null zurück.
