---
title: 列の検証の操作
type: docs
weight: 80
url: /ja/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

以前のトピックの 1 つで、検証について説明しましたが、それは[ワークシートでの検証](/cells/ja/net/working-with-validations-in-worksheets/)(検証および検証モードに関する一般的な情報については、開発者はこのトピックを参照できます)。このトピックでは、列に関する検証について説明します。この機能を使用すると、開発者はワークシートの任意の列に検証規則を適用できます。詳細に説明しましょう。

{{% /alert %}} 
## **列検証の追加**
列に任意の種類の検証を追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- **追加**望ましい**検証**任意の列に

**重要：**検証の種類 (または次のような検証モード) の詳細については、**検証が必要です**, **正規表現の検証**と**カスタム検証**）と実装**カスタム検証**、参照してください[ワークシートでの検証の操作。](/cells/ja/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **列検証へのアクセス**
特定の列の検証にアクセスするには、次の手順に従ってください。

- 希望のアクセス**ワークシート**
- 特定の列にアクセスする**検証**の中に**ワークシート**
- 編集**検証**必要に応じて属性



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **列検証の削除**
ワークシートから特定の列の検証を削除するには、次の手順に従ってください。

- 希望のアクセス**ワークシート**
- 特定の列を削除する**検証**から**ワークシート**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
