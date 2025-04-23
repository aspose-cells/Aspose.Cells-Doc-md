---  
title: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen. 
type: docs  
weight: 320  
url: /de/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Erfahren Sie, wie Sie alle versteckten Zeilenindices nach dem Aktualisieren des AutoFilters mit der API Aspose.Cells for Node.js via C++ erhalten.  
keywords: Alle versteckten Zeilenindices nach dem Aktualisieren des AutoFilters in Node.js über C++ erhalten, Alle versteckten Zeilenindices nach dem Aktualisieren des AutoFilters in Node.js über C++ abrufen, Alle versteckten Zeilenindices nach dem Aktualisieren des AutoFilters in Node.js über C++ ermitteln  
---  

## **Mögliche Verwendungsszenarien**  

Wenn Sie die AutoFilter-Funktion auf Zellen des Arbeitsblatts anwenden, werden einige Zeilen automatisch ausgeblendet. Es kann jedoch sein, dass einige Zeilen manuell vom Excel-Endbenutzer ausgeblendet wurden und nicht durch einen AutoFilter ausgeblendet werden. Daher ist es schwierig zu wissen, welche Zeilen durch den AutoFilter ausgeblendet werden und welche manuell ausgeblendet sind. Aspose.Cells for Node.js via C++ behandelt dieses Problem mit der `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die durch den AutoFilter ausgeblendet sind, jedoch nicht manuell vom Excel-Endbenutzer.  

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**  

Siehe den folgenden Beispielcode, der die [Beispiel-Excel-Datei](64716909.xlsx) lädt, die einige Zeilen enthält, die manuell vom Excel-Endbenutzer ausgeblendet wurden. Der Code wendet den AutoFilter an und aktualisiert ihn mit der `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)-Methode, die die Zeilenindizes aller durch den AutoFilter ausgeblendeten Zeilen zurückgibt. Anschließend werden die Indizes der ausgeblendeten Zeilen auf der Konsole zusammen mit Zellennamen und Werten ausgegeben.  

## **Beispielcode**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **Konsolenausgabe**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
