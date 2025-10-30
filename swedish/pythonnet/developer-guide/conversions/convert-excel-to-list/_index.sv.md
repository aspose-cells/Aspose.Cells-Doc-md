---
title: Konvertera Excel till Python data
type: docs
weight: 30
url: /sv/python-net/convert-excel-to-list/
description: Konvertera Excel till lista med hjälp av Aspose.Cells för Python via .NET API.
keywords: Konvertera Excel till dictionary med hjälp av Python Excel bibliotek, Konvertera arbetsbok till dictionary med hjälp av Python Excel bibliotek, Konvertera radobjekt till lista med hjälp av Python Excel bibliotek, Hur man konvertera ListObject till lista, Konvertera kolumnobjekt till lista med hjälp av Python Excel bibliotek, Konvertera område till lista med hjälp av Python Excel bibliotek, Konvertera kalkylblad till lista med hjälp av Python Excel bibliotek.
---

{{% alert color="primary" %}}

Med Aspose.Cells for Python via .NET API kan du konvertera arbetsbok, kalkylblad, område, rad, kolumn och annan exceldatat till Python-lista.

{{% /alert %}}

## **Hur man konverterar Excel-arbetsbok till dictionary**
Här är en kodsnutt för att visa hur man exporterar exceldatat till dictionary med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Gå igenom alla kalkylblad och konvertera arbetsbok till dictionary med hjälp av Aspose.Cells for Python Excel-bibliotek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Utmatningsresultat:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Hur man konverterar Excel-arbetsbok till lista**
Här är en kodsnutt för att visa hur man exporterar exceldatat till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Gå igenom alla kalkylblad och konvertera arbetsbok till lista med hjälp av Aspose.Cells for Python Excel-bibliotek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Utmatningsresultat:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Hur man konverterar kalkylblad till lista**
Här är en kodsnutt för att visa hur man exporterar kalkylbladsdatat till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Konvertera kalkylbladsdatat till lista med hjälp av Aspose.Cells för Python Excel-bibliotek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Utmatningsresultat:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Hur man konverterar en ListObject i Excel till lista**
Här är en kodsnutt för att visa hur man exporterar ListObject-datat till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Skapa ListObject-objekt.
1. Konvertera ListObject-data till lista med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Utmatningsresultat:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Hur man konverterar en rad i Excel till lista**
Här är ett exempelkodsnutt för att visa hur man exporterar raddata till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Hämta radobjekt efter radindex.
1. Konvertera raddata till lista med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Utmatningsresultat:
```
['Detroit', 'Central', 3074]
```

## **Hur man konverterar en kolumn i Excel till lista**
Här är ett exempelkodsnutt för att visa hur man exporterar kolumndata till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Hämta kolumnobjekt efter kolumnindex.
1. Konvertera kolumndata till lista med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Utmatningsresultat:
```
['Store', 3055, 3036, 3074]
```

## **Hur man konverterar en rad i Excel till lista**
Här är ett exempelkodsnutt för att visa hur man exporterar raddata till lista med hjälp av Aspose.Cells för Python via .NET:
1. Läs in [provfilen](sample_data.xlsx).
1. Hämta den första arbetsboken.
1. Skapa området.
1. Konvertera områdesdata till lista med hjälp av Aspose.Cells för Python Excel-biblioteket.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Utmatningsresultat:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
