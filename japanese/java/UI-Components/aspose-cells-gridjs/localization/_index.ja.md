---
title: GridJs多言語設定ガイド
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: このチュートリアルは、多言語サポートの設定方法をご案内します
keywords: GridJs、多言語、ローカリゼーション、国際化、カルチャー、CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs 多言語設定ガイド

## 概要

このチュートリアルは、Aspose.Cells GridJsプロジェクトでの多言語サポート設定方法をご案内します。フロントエンドとバックエンドの両方の設定をカバーしています。

チュートリアルは [デモプロジェクト](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs) に基づいています。実際の状況に応じて調整してください

## フロントエンド設定

フロントエンドページでは、`local` [オプション](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/) を使用してインターフェースの言語を設定します。

デモプロジェクトでは、[uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html) ファイルを修正する必要があります

次に例を示します。

```javascript
const loadNormalContext = (sheet) => {
    const option = {
        updateMode: 'server',
        updateUrl: '/GridJs2/UpdateCell',
        showToolbar: true,
        mode: 'edit',
        // Supported languages: en/zh/es/pt/de/ru/nl/pl
        local: 'pl', // Set to Polish in this example
    };
    loadWithOption(jsondata, option);
};
```

## バックエンド設定

バックエンドコードでは、Excelデータを処理する前に適切なCultureInfoを設定する必要があります。

デモプロジェクトでは、[Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)ファイルを修正する必要があります

### mainメソッドでロケール設定を行う

```java

public static void main(String[] args) {

	// Set Polish locale for current thread
        Locale polishLocale = new Locale("pl", "PL");
        Locale.setDefault(polishLocale);

        // Demonstration of locale settings
        System.out.println("Current Locale: " + Locale.getDefault());

		 ApplicationContext context  = 	SpringApplication.run(GridjsdemoApplication.class, args);

		 MyConfig myConfig = context.getBean(MyConfig.class);

		 //set license for Aspose.Cells
		 com.aspose.cells.License  lic=new com.aspose.cells.License();
			if ((new File(myConfig.asposeLicensePath)).exists()) {
				lic.setLicense(myConfig.asposeLicensePath);
			}


	}

```

## 重要な注意事項

1. フロントエンドとバックエンドの言語設定は一貫している必要があります。
2. CultureInfoはExcelデータを処理する前に設定する必要があります。
3. サポートされている言語：en（英語）、zh（中国語）、es（スペイン語）、pt（ポルトガル語）、de（ドイツ語）、ru（ロシア語）、nl（オランダ語）、pl（ポーランド語）。
4. 例ではポーランド語（pl-PL）を使用していますが、他のサポートされているロケールに変更できます。
