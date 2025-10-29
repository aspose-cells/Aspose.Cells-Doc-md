---
title: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Les API Aspose.Cells pour Python via .NET ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) en introduisant des propriétés et méthodes utiles. L'une de ces méthodes est [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) qui permet de spécifier un mot de passe sous forme d’*string* et vérifie si le même mot de passe a été utilisé pour protéger le [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

La méthode [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) renvoie **true** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée et **false** si le mot de passe spécifié ne correspond pas. Le code suivant utilise la méthode [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) en conjonction avec la propriété [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) pour détecter la protection par mot de passe et vérifie le mot de passe.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
