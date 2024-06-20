---
title: Notions de base d Aspose.Cells.GridJs
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## Notions de base de GridJs

Aspose.Cells.GridJs est une bibliothèque qui permet aux utilisateurs de développer des applications web multiplateformes pour visualiser ou modifier rapidement et facilement des fichiers de feuille de calcul. 

## Pourquoi utiliser Aspose.Cells.GridJs


- Il permet aux utilisateurs de créer, éditer, formater, collaborer et partager en toute sécurité des feuilles de calcul avec des mises à jour en temps réel, un support des formules et des outils avancés de visualisation des données, similaires aux applications de bureau traditionnelles.
- Il prend en charge la saisie et l'édition de données, le formatage, la navigation dans les feuilles de calcul, le calcul des formules, la manipulation des données, les graphiques et visualisations, l'importation et l'exportation, la sécurité, les modules complémentaires et la personnalisation pour permettre aux développeurs d'adapter l'éditeur aux besoins spécifiques de l'entreprise.

## Caractéristiques


- Importez, visualisez et modifiez les formats de feuilles de calcul populaires.
- Exportez les feuilles de calcul vers divers formats de fichier pris en charge.
- Affichez et gérez les fichiers d'image, de forme ou de graphique.
- Effectuez une conception de grille et une personnalisation de la mise en page.
- Gestion de plusieurs feuilles de calcul.
- Création et calcul des formules Excel®.

## Formats de fichiers pris en charge

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Utilisation générale

Voici les étapes de base du processus pour développer une application web de GridJs.

- Définir le répertoire de stockage du cache par Config.set_file_cache_directory(`votre chemin de stockage`)
- Définir la licence par Config.set_license(`votre chemin de licence`)
- Définir l'URL de la route de l'image GridJsWorkbook.set_image_url_base(`route pour voir l'image`)
- Mettez en place une action de route pour obtenir du `json` à partir du fichier de feuille de calcul. Vous pouvez utiliser les API `GridJsWorkbook.ImportExcelFile` et `GridJsWorkbook.ExportToJson`, `GridJs` stockera automatiquement le fichier étalé dans le cache.
- Mettez en place une action de route pour obtenir du `json` pour l'opération de mise à jour. Vous pouvez utiliser `GridJsWorkbook.UpdateCell` `API,GridJs` effectuera l'opération de mise à jour dans le cache et renverra le `json` mis à jour.
- Mettez en place une action de route pour obtenir un fichier en cache, ainsi nous pouvons obtenir le fichier zip des images/formes ou le fichier de feuille de calcul en cache.
- Mettez en place une action de route pour télécharger la feuille de calcul. Vous pouvez utiliser l'API `GridJsWorkbook.SaveToCacheWithFileName`.

Voici une démo de base pour montrer l'utilisation d'Aspose.Cells.GridJs :

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

Dans la démo, nous utilisons [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) pour le rendu de la page côté client.

Si vous avez des questions, des exigences ou avez besoin d'aide, veuillez faire part de vos commentaires sur le site suivant https://forum.aspose.com/c/cells/9
