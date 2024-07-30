---
title: Notions de base d Aspose.Cells.GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Cet article présente les étapes de base pour configurer une application web pour GridJs.
---

## Notions de base de GridJs

Aspose.Cells.GridJs est une bibliothèque standard .NET qui permet aux utilisateurs de développer rapidement et facilement des applications web pour afficher/éditer des feuilles de calcul. 

Aspose.Cells.GridJs prend en charge l'importation des formats de fichiers de feuilles de calcul populaires (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Il permet également d'exporter des fichiers Excel au format PDF, HTML, etc. Voici les étapes de base pour développer une application web avec GridJs.

- Implémentez GridCacheForStream pour écrire votre propre logique métier pour le stockage en cache.
- Configurez une action de contrôleur pour obtenir du JSON à partir du fichier de feuille de calcul. Vous pouvez utiliser les API GridJsWorkbook.ImportExcelFile et GridJsWorkbook.ExportToJson, GridJs stockera automatiquement le fichier spread en cache.
- Configurez une action de contrôleur pour obtenir du JSON pour l'opération de mise à jour. Vous pouvez utiliser l'API GridJsWorkbook.UpdateCell, GridJs effectuera l'opération de mise à jour en cache et renverra le JSON mis à jour.
- Configurez une action de contrôleur pour obtenir les URL des fichiers d'images/formes dans la feuille de calcul, GridJs zippera automatiquement toutes les images/formes en cache. Il utilisera l'API GridCacheForStream.GetFileUrl.
- Configurez une action de contrôleur pour obtenir le fichier en cache, ainsi nous pouvons obtenir le fichier zip des images/formes ou le fichier de feuille de calcul en cache. Il utilisera l'API GridCacheForStream.LoadStream.
- Mettez en place une action de contrôleur pour télécharger la feuille de calcul. Vous pouvez utiliser l'API GridJsWorkbook.SaveToCacheWithFileName.

Voici une démo de base pour montrer l'utilisation de Aspose.Cells.GridJs : https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs


Si vous avez des questions, des exigences ou avez besoin d'aide, veuillez faire part de vos commentaires sur le site suivant https://forum.aspose.com/c/cells/9
