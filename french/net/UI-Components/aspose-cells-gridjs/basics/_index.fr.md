---
title: Aspose.Cells.Bases de GridJ
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/basics/
---
## Bases de GridJs

 Aspose.Cells.GridJs est une bibliothèque standard .NET qui permet aux utilisateurs de développer une application Web pour afficher/modifier une feuille de calcul rapidement et facilement.

Aspose.Cells.GridJs prend en charge l'importation des formats de fichier de feuille de calcul populaires (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Il permet également d'exporter des fichiers Excel au format PDF, HTML .etc. Vous trouverez ci-dessous les étapes de base du processus pour développer une application Web de GridJs.

- Implémentez GridCacheForStream pour écrire votre propre logique métier pour le stockage du cache.
- Configurez une action de contrôleur pour obtenir json à partir du fichier de feuille de calcul. Vous pouvez utiliser les API GridJsWorkbook.ImportExcelFile et GridJsWorkbook.ExportToJson, GridJs stockera automatiquement le fichier de propagation dans le cache.
- Configurez une action de contrôleur pour obtenir json pour l'opération de mise à jour. Vous pouvez utiliser GridJsWorkbook.UpdateCell API, GridJs effectuera l'opération de mise à jour dans le cache et renverra le json mis à jour.
- Configurez une action de contrôleur pour obtenir l'URL des fichiers d'images/formes dans la feuille de calcul, GridJs compressera automatiquement toutes les images/formes dans le cache. Il utilisera GridCacheForStream.GetFileUrl API.
- Configurez une action du contrôleur pour obtenir le fichier dans le cache, ainsi nous pouvons obtenir le fichier zip des images/formes ou le fichier de feuille de calcul dans le cache. Il utilisera GridCacheForStream.LoadStream API.
- Configurez une action de contrôleur pour télécharger la feuille de calcul. Vous pouvez utiliser GridJsWorkbook.SaveToCacheWithFileName API.

 Voici une démo de base pour montrer l'utilisation de Aspose.Cells.GridJs : https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

Si vous avez des questions, des exigences ou avez besoin d'aide, veuillez nous faire part de vos commentaires sur le site Web suivant https://forum.aspose.com/c/cells/9