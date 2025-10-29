---
title: Intégration du plugin AI
type: docs
weight: 35
url: /fr/python-net/ai-plugin-integration/
description: Intégrer Aspose.Cells pour Python via .NET aux outils d IA.
keywords: MarkItDown, Marker et Docling, convertir Excel en JSON, MD et HTML.
---

# Intégration du plugin AI

Ce document résume trois outils de traitement de documents alimentés par l'IA—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker), et [Docling](https://github.com/docling-project/docling)—mettant en évidence leurs fonctionnalités communes d'IA et leur intégration avec [Aspose.Cells pour Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) via des plugins.

---

## 1. Common AI Features

### 1.1 Multi-format Document Parsing and Structured Representation
All three projects support parsing multiple document formats, including PDF, DOCX, PPTX, XLSX, HTML, etc., and converting them into structured formats (Markdown, JSON, or HTML) suitable for AI processing.

- **MarkItDown**: Converts documents into Markdown format, easily integrated with LLMs and text analysis pipelines.  
- **Marker**: Supports Markdown, JSON, and HTML output while preserving tables, formulas, and other content.  
- **Docling**: Provides a unified `DoclingDocument` representation, supporting multi-format document parsing and structured export.

### 1.2 Integration with Generative AI Frameworks
All three tools support integration with generative AI frameworks to enhance document processing capabilities:

- **MarkItDown**: Integrates with Azure OpenAI to improve document and image processing.  
- **Marker**: Supports leveraging large language model (LLM) technology to improve the accuracy of document processing.  
- **Docling**: Compatible with frameworks like LangChain, LlamaIndex, and Haystack for agentic AI applications.

---

## 2. Intégration du plugin Aspose.Cells pour Python via .NET

Pour combiner les données Excel avec ces outils de traitement de documents AI, nous avons développé des plugins dédiés pour chaque outil :

| Plugin | Dépôt | Fonctionnalité |
|--------|------------|---------------|
| Plugin MarkItDown | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Convertit les fichiers Excel en format Markdown. |
| Plugin Marker | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Convertit les fichiers Excel en formats supportés par Marker (Markdown, JSON ou HTML), en utilisant le mode LLM de Marker pour une meilleure table. |
| Plugin Docling | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Convertit les fichiers Excel en objets `DoclingDocument`, puis exporte en Markdown, JSON ou HTML pour une analyse multimodale. |

### 2.1 Avantages du plugin

1. **Conversion Excel Rapide** : Convertit rapidement le contenu Excel en Markdown, JSON ou HTML pour le traitement par l'IA.  
2. **Préservation des Informations de Table et de Format** : Conserve essentiellement les données de la table originale pour assurer l'intégrité des données.  
3. **Compatible avec les Outils d'IA** : Peut être directement utilisé comme entrée pour MarkItDown, Marker ou Docling, en tirant parti de fonctionnalités avancées de parsing.  
4. **Installation Facile** : Nécessite simplement l'installation supplémentaire d'Aspose.Cells pour Python via .NET(aspsoe-cells-python) et suivre les instructions du README dans les répertoires des plugins.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Vérifier l'installation :
```bash
markitdown --list-plugins
```
Convertir un fichier XLSX en utilisant le plugin :
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 Plugin Marker

Vous aurez besoin de Python 3.10+ et [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
Pour les documents non-PDF, installez toutes les dépendances :
```
pip install marker-pdf[full]
```

Convertir un seul fichier :
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Plugin Docling

Installer Docling :
```
pip install -e .
```

Convertir les fichiers Excel en différents formats :
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Des [instructions d'installation plus détaillées](https://docling-project.github.io/docling/installation/) sont disponibles dans la documentation.

### 3.4 Définir la licence Aspose

Avant d'utiliser Aspose.Cells dans un plugin, configurez la licence :

Windows (PowerShell) :
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD) :
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Systèmes Unix :
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Résumé

#### Fonctionnalités IA :
Les trois outils partagent des avantages communs dans l'analyse de documents IA, sortie structurée, support multimodal, et intégration avec des frameworks d'IA générative.

#### Plugins Aspose.Cells :
Permet la conversion transparente des données Excel en Markdown, JSON ou HTML, en conservant les tableaux, formules et une intégration directe avec MarkItDown, Marker ou Docling.

#### Cas d'utilisation :
Idéal pour le traitement intelligent de documents, la construction de bases de connaissances, les systèmes RAG, l’analyse de rapports, la conversion de documents académiques et autres workflows basés sur l’IA.

{{< app/cells/assistant language="python-net" >}}
