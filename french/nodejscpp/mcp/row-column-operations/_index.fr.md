---
title: Opérations sur lignes et colonnes Excel
linktitle: Opérations sur lignes et colonnes
type: docs
weight: 50
url: /fr/nodejs-cpp/mcp/row-column-operations
keywords: "Opérations sur lignes Excel, opérations sur colonnes Excel, gestion de la disposition Excel, insérer des lignes, supprimer des colonnes, redimensionner les cellules Excel"
description: "Opérations sur lignes et colonnes Excel  insérer, supprimer, redimensionner, masquer/afficher lignes et colonnes avec automatisation par IA"
---

# Opérations sur lignes et colonnes Excel

Gérez les **opérations sur lignes et colonnes Excel** avec une automatisation alimentée par l'IA. Insérez, supprimez, redimensionnez, masquez/affichez les **lignes Excel** et **colonnes** pour une gestion parfaite de la disposition du tableau.

## Outils disponibles

- `row_column_operations` - **Opérations sur lignes/colonnes Excel** (insérer, supprimer, redimensionner, masquer/afficher) avec **Excel IA**
- `row_column_operations_batch` - Effectuer plusieurs **opérations sur lignes/colonnes Excel** en lot en utilisant **Excel MCP**

## Opérations uniques

### Insérer des lignes
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

### Supprimer des colonnes
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

### Régler la hauteur des lignes
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

### Définir la largeur de la colonne
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

## Opérations par lot

### Configuration complète de la mise en page
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

### Opérations d'insertion et de suppression
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

### Opérations de masquage et d'affichage
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

### Opérations d'auto-ajustement
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

## Référence des types d'opérations

### Opérations d'insertion
- `insert_rows` - Insérer de nouvelles lignes à une position spécifique
- `insert_columns` - Insérer de nouvelles colonnes à une position spécifique

### Opérations de suppression  
- `delete_rows` - Supprimer les lignes spécifiées
- `delete_columns` - Supprimer les colonnes spécifiées

### Opérations de redimensionnement
- `set_row_height` - Définir la hauteur spécifique d'une ligne en points
- `set_column_width` - Définir la largeur spécifique d'une colonne en caractères
- `auto_fit_rows` - Ajuster automatiquement la hauteur des lignes au contenu
- `auto_fit_columns` - Ajuster automatiquement la largeur des colonnes au contenu

### Opérations de visibilité
- `hide_rows` - Masquer les lignes spécifiées
- `unhide_rows` - Montrer les lignes masquées
- `hide_columns` - Masquer les colonnes spécifiées
- `unhide_columns` - Montrer les colonnes masquées

## Spécifications de la plage

### Plages de lignes
- `"1"` - Ligne unique (ligne 1)
- `"1:3"` - Plage de lignes (lignes 1 à 3)
- `"5:10"` - Plusieurs lignes consécutives

### Plages de colonnes
- `"A"` - Colonne unique (colonne A)
- `"A:C"` - Plage de colonnes (colonnes A à C)
- `"D:F"` - Plusieurs colonnes consécutives

## Exemples avancés

### Configuration de l’en-tête du rapport
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

### Mise en page du tableau de données
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

### Mise en page de la présentation
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

## Directives de mesure

### Hauteurs des lignes (points)
- `15` - Hauteur de ligne par défaut
- `20` - Légèrement plus grande pour une meilleure lisibilité
- `25` - Bon pour les en-têtes
- `30` - En-têtes de grande taille
- `40` - Très grand pour les titres

### Largeurs de colonnes (caractères)
- `8` - Colonnes étroites (dates, codes)
- `12` - Colonnes de données standard
- `15` - Colonnes de texte moyennes
- `20` - Colonnes de texte larges
- `25` - Très larges pour descriptions
- `30` - Très larges pour longs textes

## Bonnes pratiques

1. **Taille de l'en-tête** : Rendre les en-têtes plus grands et plus larges pour l'accentuation
2. **Cohérence des données** : Utiliser des hauteurs de lignes cohérentes pour les lignes de données
3. **Ajustement automatique** : Utiliser l'ajustement automatique pour la taille du contenu dynamique
4. **Masquer les inutilisés** : Masquer les lignes/colonnes vides pour une apparence plus propre
5. **Regroupement logique** : Regrouper les opérations de redimensionnement liées par lots

## Schémas courants

### Schéma de configuration du rapport
1. Insérer des lignes de titre en haut
2. Définir la hauteur de la ligne d'en-tête
3. Ajuster automatiquement les colonnes de données
4. Définir la hauteur standard des lignes de données
5. Masquer les zones inutilisées

### Modèle d'importation de données
1. Insérer des lignes pour de nouvelles données
2. Ajuster automatiquement les colonnes au contenu
3. Standardiser la hauteur des lignes
4. Masquer les colonnes de calcul

### Modèle de présentation
1. Masquer les lignes/colonnes de détail
2. Agrandir les zones de résumé
3. Définir des dimensions adaptées à la présentation
4. Afficher uniquement les données pertinentes

## Gestion des erreurs

### Plage de lignes invalide
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
**Résultat** : Erreur - les numéros de ligne commencent à 1

### Plage de colonnes invalide
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
**Résultat** : Peut réussir mais en dehors de la utilisation typique

### Paramètres obligatoires manquants
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
**Résultat** : Erreur - le paramètre hauteur est requis 
{{< app/cells/assistant language="nodejs-cpp" >}}
