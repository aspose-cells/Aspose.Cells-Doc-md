---
title: Konvertera Excel till NumPy
type: docs
weight: 30
url: /sv/python-net/convert-excel-to-numpy/
description: Konvertera Excel till NumPy genom att använda Aspose.Cells för Python via .NET API.
keywords: Python Konvertera Excel till NumPy arrayer, Exportera kalkylbok till NumPy arrayer i Python via NET, Python Konvertera Rad till NumPy array, Python Konvertera Tabell till NumPy arrayer, Exportera ListObject till NumPy array i Python via NET, Python Konvertera Område till NumPy array, Kolumn till NumPy array med hjälp av Python.
---

## **Introduktion till NumPy**
NumPy (Numerical Python) är en öppen källkods-numerisk datortillägg till Python. Detta verktyg kan användas för att lagra och bearbeta stora matriser, vilket är mycket mer effektivt än Pythons nästlade liststruktur (som också kan användas för att representera matriser). Det stöder ett stort antal dimensionella matriser och matrisoperationer, och tillhandahåller också ett stort antal matematiska funktionsbibliotek för matrisoperationer. 

NumPys huvudfunktioner:
1. Ndarray, en flerdimensionell matrisobjekt, är en snabb, flexibel och platsbesparande datastruktur.
1. Linjär algebraoperationer, inklusive matrismultiplikation, transposition, invertering, etc.
1. Fouriertansformation, utföra en snabb fouriertansformation på en matris.
1. Snabb operation av flyttalsmatriser.
1. Integrera C-språkkod i Python för att få det att köra snabbare.

Genom att använda Aspose.Cells för Python via .NET API kan du konvertera Excel, TSV, CSV, Json och många olika format till Numpy ndarray.

## **Hur man konverterar Excel-arbetsbok till NumPy ndarray**
Här är en exempelkodsnutt för att demonstrera hur man exporterar exceldatan till en NumPy-matris med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Gå igenom exceldatan och exportera datan till NumPy-matris med hjälp av Aspose.Cells för Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Utmatningsresultat:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Hur man konverterar arbetsblad till NumPy ndarray**
Här är en exempelkodsnutt för att demonstrera hur man exporterar arbetsbladsdata till Numpy ndarray med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Konvertera arbetsbladsdata till Numpy ndarray med hjälp av Aspose.Cells för Python Excel-bibliotek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Utmatningsresultat:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Hur man konverterar en Excels område till NumPy ndarray**
Här är en exempelkodsnutt för att demonstrera hur man exporterar områdesdata till NumPy ndarray med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Skapa området.
1. Konvertera områdesdata till Numpy ndarray med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Utmatningsresultat:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Hur man konverterar ett ListObject i Excel till NumPy ndarray**
Här är en exempelkodsnutt för att demonstrera hur man exporterar ListObject-datan till Numpy ndarray med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Skapa ListObject-objekt.
1. Konvertera ListObject-data till NumPy ndarray med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Utmatningsresultat:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Hur man konverterar en rad i Excel till NumPy ndarray**
Här är ett exempel på kodsnutt för att visa hur man exporterar raddata till NumPy ndarray med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Hämta radobjekt efter radindex.
1. Konvertera raddata till NumPy ndarray med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Utmatningsresultat:
```
['Detroit' 'Central' '3074']
```

## **Hur man konverterar en kolumn i Excel till NumPy ndarray**
Här är ett exempel på kodsnutt för att visa hur man exporterar kolumnedata till NumPy ndarray med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Hämta kolumnobjekt efter kolumnindex.
1. Konvertera kolumndata till NumPy ndarray med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Utmatningsresultat:
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
