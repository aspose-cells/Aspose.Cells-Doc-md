---
title: Excel rad och kolumnoperationer
linktitle: Rad och kolumnoperationer
type: docs
weight: 50
url: /sv/nodejs-cpp/mcp/row-column-operations
keywords: "Excel radoperationer, Excel kolumnoperationer, Excel layouthantering, infoga rader, ta bort kolumner, ändra storlek på Excel celler"
description: "Excel rad och kolumnoperationer  infoga, ta bort, ändra storlek, göm/visa rader och kolumner med AI automatisering"
---

# Excel rad- och kolumnoperationer

Hantera **Excel rad- och kolumnoperationer** med AI-driven automatisering. Infoga, ta bort, ändra storlek på, göm/visa **Excelrader** och **kolumner** för perfekt kalkylblads layouthantering.

## Tillgängliga Verktyg

- `row_column_operations` - **Excel rad/kolumnoperationer** (infoga, ta bort, ändra storlek, göm/visa) med **AI Excel**
- `row_column_operations_batch` - Utför flera **Excel rad/kolumnoperationer** i batch med **Excel MCP**

## Enskilda operationer

### Infoga rader
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### Ta bort kolumner
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### Ställ in radhöjd
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### Sätt kolumnbredd
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## Batchoperationer

### Omfattande layoutinställning
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### Infoga- och ta bortoperationer
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### Dölj och visa operationer
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### Autopassningsoperationer
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## Referens för operationstyper

### Infogningsoperationer
- `insert_rows` - Infoga nya rader på angiven position
- `insert_columns` - Infoga nya kolumner på angiven position

### Rader- och kolumnborttagning  
- `delete_rows` - Ta bort angivna rader
- `delete_columns` - Ta bort angivna kolumner

### Ändra storlek-operationer
- `set_row_height` - Ange specifik radhöjd i punkter
- `set_column_width` - Ange specifik kolumnbredd i tecken
- `auto_fit_rows` - Auto-anpassa rader till innehållets höjd
- `auto_fit_columns` - Auto-anpassa kolumner till innehållets bredd

### Visibility operations
- `hide_rows` - Dölj angivna rader
- `unhide_rows` - Visa dolda rader
- `hide_columns` - Dölj angivna kolumner
- `unhide_columns` - Visa dolda kolumner

## Områdespecifikationer

### Radintervall
- `"1"` - Enskild rad (rad 1)
- `"1:3"` - Radintervall (raderna 1 till 3)
- `"5:10"` - Flera på varandra följande rader

### Kolumnintervall
- `"A"` - Enskild kolumn (kolumn A)
- `"A:C"` - Kolumnintervall (kolumner A till C)
- `"D:F"` - Flera på varandra följande kolumner

## Avancerade exempel

### Rapporthuvuduppsättning
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### Datatabellayout
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### Presentationslayout
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## Mätning riktlinjer

### Radhöjder (Poäng)
- `15` - Standard radhöjd
- `20` - Något högre för läsbarhet
- `25` - Bra för rubriker
- `30` - Stora rubriker
- `40` - Extra stort för titlar

### Kolumnbredder (Tecken)
- `8` - Smala kolumner (datum, koder)
- `12` - Standard datakolumner
- `15` - Medeltextkolumner
- `20` - Bred textkolumner
- `25` - Extra bred för beskrivningar
- `30` - Mycket bred för långt text

## Bästa praxis

1. **Rubrikstorlek**: Gör rubrikerna högre och bredare för betoning
2. **Datakonsistens**: Använd konsekventa radhöjder för datarad
3. **Automatisk anpassning**: Använd auto-anpassning för dynamisk innehållsstorlek
4. **Dölj oanvänd**: Dölj tomma rader/kolumner för ett renare utseende
5. **Logisk gruppering**: Grupper relaterade storleksändringsoperationer i batchar

## Vanliga mönster

### Rapportuppsättningsmönster
1. Infoga titellinjer överst
2. Ställ in rubrikradens höjd
3. Auto-anpassa datakurvor
4. Sätt standardhöjd för data rader
5. Dölj oanvända områden

### Dataimportmönster
1. Infoga rader för ny data
2. Auto-anpassa kolumner till innehåll
3.Standardisera radhöjder
4. Dölj beräkningskolumner

### Presentationsmönster
1. Dölj detalj rader/kolumner
2. Förstora sammanfattningsområden
3. Sätt presentationsvänliga dimensioner
4. Visa endast relevant data

## Felhantering

### Ogiltigt radintervall
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**Resultat**: Fel - radnummer börjar från 1

### Ogiltigt kolumnintervall
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**Resultat**: Kan lyckas men utanför vanlig användning

### Saknade kravparametrar
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**Resultat**: Fel - höjdparameter krävs 
{{< app/cells/assistant language="nodejs-cpp" >}}
