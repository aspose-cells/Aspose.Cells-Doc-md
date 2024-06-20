---
title: 列での検証の処理
type: docs
weight: 80
url: /ja/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop、validation、validations
description: この記事では、GridDesktopで列で検証を使用する方法について紹介します。
---

{{% alert color="primary" %}} 

以前のトピックの1つで、[ワークシートでの検証を使用する](/cells/ja/net/working-with-validations-in-worksheets/) について説明しました（検証や検証モード（必須検証、正規表現検証、カスタム検証）の種類とカスタム検証の実装について詳しくはこのトピックを参照してください）。 このトピックでは、列に関連して検証を説明します。 この機能を使用すると、開発者はワークシートの任意の列に検証ルールを適用できます。 詳しく説明します。

{{% /alert %}} 
## **列の検証の追加**
列に検証を追加するには、以下の手順に従ってください：

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- 任意の列に**検証**を**追加**します

**重要：** 検証の種類（または**必須検証**、**正規表現検証**、**カスタム検証**の検証モード）や**カスタム検証**の詳細については、[ワークシートでの検証を使用する](/cells/ja/net/working-with-validations-in-worksheets/)を参照してください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **列の検証へのアクセス**
特定の列の検証にアクセスするには、以下の手順に従ってください：

- 希望の **Worksheet** にアクセス
- ワークシート内の特定の列の**検証**にアクセスします
- 必要に応じて **Validation** 属性を編集



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **列の検証の削除**
ワークシートから特定の列検証を削除するには、以下の手順に従ってください：

- 希望の **Worksheet** にアクセス
- **ワークシート**から特定の列の**検証**を削除します



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
