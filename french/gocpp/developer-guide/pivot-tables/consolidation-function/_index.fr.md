---
title: Fonction de consolidation avec Golang via C++
linktitle: Fonction de consolidation
type: docs
weight: 20
url: /fr/go-cpp/consolidation-function/
description: Apprenez comment appliquer la fonction de consolidation aux champs de données d un tableau croisé dynamique à l aide d Aspose.Cells avec Golang via C++.
---

## **Fonction de consolidation**

Aspose.Cells peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou aux champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres du champ de valeur...** et ensuite sélectionner l'onglet **Recapituler les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme Somme, Nombre, Moyenne, Max, Min, Produit, Nombre distinct, etc.

Aspose.Cells fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/) pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction::Moyenne
- ConsolidationFunction::Compte
- ConsolidationFunction::CountNums
- ConsolidationFunction::CompteDistincts
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Produit
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Somme
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Application de la fonction de consolidation aux champs de données d'un tableau croisé dynamique**

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **Nombre distinct** au deuxième champ de données (ou champ de valeur).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

La fonction de consolidation ComptageDistinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}
