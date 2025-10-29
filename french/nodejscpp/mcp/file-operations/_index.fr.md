---
title: Fichier Excel et opérations sur les données
linktitle: Fichier et opérations sur les données
type: docs
weight: 10
url: /fr/nodejs-cpp/mcp/file-operations
keywords: « opérations sur les fichiers Excel, opérations sur les données Excel, créer un classeur Excel, feuille de calcul Excel, lire les données Excel, écrire des données Excel »
description: « opérations sur les fichiers et données Excel  créer des classeurs, gérer des feuilles de calcul, lire et écrire des données Excel avec automatisation IA »
---

# Opérations sur les fichiers et données Excel

Gérez **fichiers Excel** et **opérations sur les données** avec une automatisation alimentée par l'IA. Créez des **classeurs Excel**, gérez des **feuilles** et effectuez des opérations **lecture/écriture** de **données Excel**.

## Outils disponibles

- `create_workbook` - Créez de nouveaux ** classeurs Excel ** avec une automatisation **AI Excel**
- `create_worksheet` - Ajoutez des **feuilles de calcul Excel** à des **classeur Excel** existants
- `get_workbook_info` - Obtenez des métadonnées et des informations sur le **classeur Excel**
- `read_data_from_excel` - Lire des données à partir de **feuilles Excel** avec une précision alimentée par **IA**
- `write_data_to_excel` - Écrire des données dans des **feuilles Excel** via **Excel MCP**

## Créer des classeurs Excel

### Créer un classeur de base
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Créer un classeur avec une feuille personnalisée
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Gérer les feuilles de calcul

### Ajouter une nouvelle feuille
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Obtenir des informations sur le classeur
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Écrire des données Excel

### Écrire des en-têtes et des données
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Écrire des données à une position personnalisée
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Lire les données Excel

### Lire toute la plage utilisée
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Lire une plage spécifique
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Lire à partir de la position par défaut
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Exemple de workflow complet

### 1. Créer votre premier rapport Excel
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Ajouter une feuille de résumé
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Écrire des données de vente
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Vérifier les données
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Vérifier la structure du classeur
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Meilleures pratiques

1. **Chemins de fichiers** : Utilisez des chemins relatifs pour une meilleure portabilité
2. **Noms des feuilles** : Utilisez des noms descriptifs pour les feuilles de calcul
3. **Structure des données** : Organisez les données avec des en-têtes clairs
4. **Lecture de plages** : Spécifiez les plages pour de grands ensembles de données
5. **Gestion des erreurs** : Vérifiez l'existence du fichier avant les opérations

## Modèles courants

### Modèle d'importation de données
1. Créer un classeur
2. Écrire les données brutes
3. Vérifier en lisant à nouveau
4. Traitement avec des formules

### Rapports multi-feuilles
1. Créer un classeur avec la feuille principale
2. Ajouter des feuilles de résumé/d’analyse
3. Écrire les données dans chaque feuille
4. Lier les feuilles avec des formules

### Validation des données
1. Écrire les données
2. Lire à nouveau des plages spécifiques
3. Vérifier l’intégrité des données
4. Gérer les valeurs manquantes 
{{< app/cells/assistant language="nodejs-cpp" >}}
