---
title: Benutzerdefinierte Zeilen- und benutzerdefinierte Spaltenüberschrift des GridDesktop-Arbeitsblatts
type: docs
weight: 120
url: /de/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **Mögliche Nutzungsszenarien**
Sie können die Zeilen- und Spaltenbeschriftung des GridDesktop-Arbeitsblatts anpassen. Normalerweise beginnt die Zeile bei 1 und die Spalte bei A. Sie können dieses Verhalten ändern und Ihre eigenen Beschriftungen für Zeilen und Spalten des GridDesktop-Arbeitsblatts verwenden. Um die Beschriftungen von Zeilen und Spalten zu ändern, implementieren Sie bitte die Schnittstellen ICustomRowCaption und ICustomColumnCaption.
## **Benutzerdefinierte Zeilen- und benutzerdefinierte Spaltenüberschrift des GridDesktop-Arbeitsblatts**
Der folgende Beispielcode implementiert die Schnittstellen ICustomRowCaption und ICustomColumnCaption und ändert die Beschriftungen von Zeilen und Spalten. Der Screenshot zeigt das Ergebnis der Ausführung dieses Beispielcodes für eine Referenz.



![todo: Bild_alt_Text](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
