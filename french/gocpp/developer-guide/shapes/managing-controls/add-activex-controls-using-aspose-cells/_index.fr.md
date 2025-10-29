---
title: Ajouter des contrôles ActiveX en utilisant Aspose.Cells avec Golang via C++
linktitle: Ajouter des contrôles ActiveX
type: docs
weight: 260
url: /fr/go-cpp/add-activex-controls-using-aspose-cells/
description: Apprenez comment ajouter des contrôles ActiveX aux feuilles de calcul Excel de manière programmatique en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) qui spécifie le type de contrôle ActiveX à ajouter dans une feuille de calcul. Les valeurs suivantes sont disponibles :

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Inconnu

Une fois que vous avez ajouté le contrôle ActiveX dans la collection de formes, vous pouvez accéder à l'objet contrôle ActiveX via la méthode [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) et définir ses diverses propriétés.

{{% /alert %}}

Le code d'exemple suivant ajoute un contrôle ActiveX de bouton bascule en utilisant Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
