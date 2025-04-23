---
title: Versionnage
type: docs
weight: 40
url: /fr/go-cpp/versioning/
description: Comment installer Aspose Cells pour Go via C++ et créer une application Hello World.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** est un chemin de module Go qui spécifie une version particulière d'une bibliothèque tierce. Analysons ce chemin de module et expliquons sa signification :
Découpage du chemin du module

1. **Adresse du dépôt GitHub** : github.com/aspose-cells/aspose-cells-go-cpp

- Cette partie indique que la bibliothèque est hébergée sur GitHub, sous l'organisation ou l'utilisateur aspose-cells, dans le dépôt nommé aspose-cells-go-cpp.
- Aspose.Cells est une suite d'API pour gérer et manipuler des fichiers de tableaux (comme Excel).

1. **Numéro de version** : /v25

- /v25 indique que c'est la version 24 de la bibliothèque. Dans les modules Go, la version sémantique (SemVer) est prise en charge, où les chemins contenant /vN sont utilisés pour préciser explicitement le numéro de version principale.
- Lorsque la version principale est supérieure ou égale à 2, le chemin du module doit inclure le numéro de version pour garantir la compatibilité et l’isolation entre différentes versions principales.

### **Signification**

- **aspose-cells-go-cpp** : Il s'agit d'un liaison Go pour une bibliothèque C++, vous permettant d'utiliser les fonctionnalités d'Aspose.Cells dans vos programmes Go pour lire, écrire et manipuler des fichiers Excel, entre autres opérations.
- **v25** : Cela indique que vous référencez la version 24 de la bibliothèque. Différentes versions principales peuvent introduire des changements incompatibles, il est donc crucial de préciser le numéro de version pour que votre projet dépende de l'API et du comportement corrects.

### **Utilisation**

Pour utiliser aspose-cells-go-cpp v25 dans votre projet Go, vous devez ajouter la ligne suivante dans le fichier go.mod de votre projet :

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

Remplacez v25.x.x par les numéros de version mineure et de patch spécifiques, par exemple v25.0.0. Vous pouvez ajouter et télécharger automatiquement cette dépendance avec la commande go get :

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
