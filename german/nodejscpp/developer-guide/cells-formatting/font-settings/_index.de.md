---  
title: Schrift Einstellungen mit Node.js über C++  
linktitle: Schriftart Einstellungen  
description: Aspose.Cells ist eine Node.js Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Schriftarteinstellungen von Zellen, sodass Benutzer den Schriftstil und die Eigenschaften der Zellen anpassen können. Dieser Artikel stellt vor, wie man die Aspose.Cells Bibliothek verwendet, um die Schriftarteinstellungen von Zellen festzulegen.  
keywords: Aspose.Cells, Zellen, Schriftarteinstellungen, Stile, Eigenschaften, Node.js über C++  
type: docs  
weight: 30  
url: /de/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
Das Erscheinungsbild eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können den Namen, den Stil, die Größe, die Farbe und andere Effekte der Schriftarten umfassen. Ganz wie Microsoft Excel unterstützt auch Aspose.Cells das Konfigurieren der Schriftarteinstellungen von Zellen.  
{{% /alert %}}  

## **Konfigurieren von Schriftarteinstellungen**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse dar.  

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse mit den [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) und [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-Methoden, die zum Abrufen und Festlegen des Formatierungsstils einer Zelle verwendet werden. Die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Klasse bietet Eigenschaften zum Konfigurieren der Schriftarteinstellungen.  

### **Schriftartname festlegen**  

Entwickler können jede Schriftart auf Text innerhalb einer Zelle anwenden, indem sie die [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-Objekt-[setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) Methode verwenden.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Schriftschnitt auf Fett setzen**  

Entwickler können den Text fett machen, indem sie die [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-Objekt [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) Methode auf **true** setzen.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Schriftgröße festlegen**  

Stellen Sie die Schriftgröße mit der [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-Objekt [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-)-Methode ein.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Schriftfarbe festlegen**  

Verwenden Sie die [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-Objekt [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-)-Methode, um die Schriftfarbe festzulegen. Wählen Sie eine beliebige Farbe aus der Enum-Collection Color (Teil von Node.js) und weisen Sie sie der Methode [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) zu.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Schriftart-Unterstrich-Typ festlegen**  

Verwenden Sie die [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) Objekt- [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) Methode, um Text zu unterstreichen. Aspose.Cells bietet verschiedene vordefinierte Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype) Enumeration.  

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|  
| :- | :- |  
|Accounting|Einzelne Buchhaltungsunterstreichung|  
|Double|Doppelte Unterstreichung|  
|DoubleAccounting|Doppelte Buchhaltungsunterstreichung|  
|None|Keine Unterstreichung|  
|Single|Einfache Unterstreichung|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Einstellung des Durchgestrichen-Effekts**  

Strichen Sie durch, indem Sie die [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) Objekt- [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) Methode auf **true** setzen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Einstellen des Tiefgestellt-Effekts**  

Apply subscript by setting the [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) object's [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) method to **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Einstellen des Hochgestellt-Effekts auf Schriftart**  

Entwickler können den Hochstelleneffekt auf die Schriftart anwenden, indem sie die [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) Methode des [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) Objekts auf **true** setzen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Erweiterte Themen**  
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


