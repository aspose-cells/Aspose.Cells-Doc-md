---
title: ヘッダーとフッターのスマートマーカー | Aspose.Cells for Java
linktitle: ヘッダー・フッターのスマートマーカー | Aspose.Cells
description: Aspose.Cells for Java で、二重山括弧構文と WorkbookDesigner.setEnableHeaderFooterMarkers スイッチを使用し、Getter Bean リストまたは JSON データソースを利用してページのヘッダーとフッターに Smart Marker プレースホルダーを配置し、データ URI を介して画像をバインドできます。
keywords: Aspose.Cells for Java, スマートマーカー, ヘッダー, フッター, ヘッダー フッターマーカー, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, Getter Bean, JSON データソース, データ バインディング, 画像, データ URI, Java
type: docs
weight: 196
url: /ja/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ページのヘッダーとフッターには、レポートタイトル、報告期間、作成者、部門などのメタデータが頻繁に含まれます。これらの情報がワークブックにデータを投入する際にすでに存在している場合、手動で繰り返し入力すると不要な重複が発生します。  
従来の Smart Marker 構文 `&=Source.Field` はワークシート本体のセルで処理されます。`PageSetup.setHeader` または `PageSetup.setFooter` でヘッダーやフッターに従来マーカーを配置した場合、`WorkbookDesigner.process()` が走査するセルグリッドに含まれないため文字列のまま残ります。  
**Aspose.Cells for Java 26.11** 以降、`WorkbookDesigner` のヘッダー/フッターマーカーオプションは既定で `false` です。`designer.setEnableHeaderFooterMarkers(true)` を `designer.process()` の前に呼び出すことで、ヘッダーとフッターの文字列内に記述された `<<Source.Field>>` プレースホルダーを解決できます。ヘッダー/フッターのプレースホルダーは本体マーカーと同じデータソースを使用します。  
各ヘッダーとフッターは次の 3 つのアドレス可能なセクションで構成されます。
- セクション `0` は左側のセクションです。
- セクション `1` は中央のセクションです。
- セクション `2` は右側のセクションです。  
`PageSetup.setHeader(int section, String value)` と `PageSetup.setFooter(int section, String value)` を使用してこれらのセクションに書き込みます。処理後は `PageSetup.getHeader(int section)` と `PageSetup.getFooter(int section)` で完成したテキストを取得できます。

{{% alert color="primary" %}}
`<<Source.Field>>` のようなプレースホルダーは、フィールドの値をテキストとしてセクション文字列に挿入します。画像は `(picture)` サフィックスとデータ URI の値でバインドされます。
{{% /alert %}}

## **Getter Bean リストでヘッダー/フッターマーカーを有効にする**
**Aspose.Cells for Java 26.11** で Getter Bean リストを使用してヘッダーとフッターのプレースホルダーを解決する手順は次のとおりです。
1. `Workbook` を作成し、インデックス `0` の最初の `Worksheet` を取得します（例: `workbook.getWorksheets().get(0)`）。
2. `PageSetup.setHeader` と `PageSetup.setFooter` を使用して、目的のヘッダーおよびフッターセクションに `<<Source.Field>>` プレースホルダーを書き込みます。
3. 各プレースホルダー フィールドに対応する getter（例: `getName()`）を持つ小さな PUBLIC Bean クラスを定義し、プレースホルダーで使用するプレフィックスに一致するソース名を選択します。たとえば、`node` というソース名は `<<node.Name>>` のようなプレースホルダーを裏付けます。このプラットフォームでは次の 2 つのバインディング規則が確認されています。public フィールドだけの Bean は何もバインドされず（エンジンは getter を読み取ります）、PACKAGE-PRIVATE クラスもバインドされません。インテロスペクションは public クラスのみを認識し、非public Bean は `process()` 時に NullPointerException をスローします。
4. ワークブック用に `WorkbookDesigner` を作成します。
5. 処理前に `designer.setEnableHeaderFooterMarkers(true)` を呼び出します。
6. `designer.setDataSource("node", table)` でリストとそのソース名を関連付けます。
7. `designer.process()` を呼び出します。
8. 処理後、ヘッダーまたはフッターのテキストにプレースホルダーは残りません。完成したセクション文字列は `PageSetup.getHeader` と `PageSetup.getFooter` で取得できます。

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **JSON データソースの使用**
レポートデータがすでに JSON 形式で利用可能な場合は、Getter Bean リストの代わりに JSON を使用できます。`WorkbookDesigner.setJsonDataSource(String name, String json)` を呼び出してソースを添付します。  
`name` 引数はプレースホルダーで使用するソース名です。たとえば、`node` という名前は `<<node.Company>>` や `<<node.Title>>` のプレースホルダーを裏付けます。  
`setJsonDataSource` には行データを直接渡します。
- 行の配列（1 行以上のオブジェクトを含む JSON 配列）をサポートします。
- 1 行オブジェクトを直接渡すことも可能です。
- `{"rows":[...]}` のように名前付きトップレベルキーで行をラップしないでください。このラッパーはこのワークフローが期待する行指向の入力形状ではありません。  
1 つの JSON ソースで、同じ `designer.process()` 呼び出し中に本体セルの従来 `&=` マーカーとヘッダー/フッターセクションの二重山括弧 `<<>>` プレースホルダーの両方を解決できます。ヘッダー/フッターのプレースホルダーを解決するには、引き続き `EnableHeaderFooterMarkers` を有効にする必要があります。

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **スイッチとマルチ行ソースのセマンティクス**
`EnableHeaderFooterMarkers` 設定は既定で `false` であり、スイッチはヘッダーおよびフッターの `<<Source.Field>>` プレースホルダーだけを制御します。スイッチがオフの場合、`designer.process()` は本体セルの従来 `&=` マーカーは解決しますが、ヘッダーまたはフッター内の `<<Source.Field>>` プレースホルダーは文字列のまま残ります。  
ヘッダーまたはフッターのセクションは 1 つの文字列であり、繰り返しバンドではありません。データソースに複数行が含まれている場合、最初の行がヘッダーとフッターの値を供給します。解決後、これらの値は通常のヘッダーまたはフッターテキストとなり、`workbook.save(...)` で保存した後に再度ロードしても保持されます。  
以下の例は、同じマルチ行 Bean リストを使用して 2 つのワークブックを作成し、無効状態と有効状態の動作を比較しています。`plainDesigner` はプレースホルダーを変更せずに残し、`enabledDesigner` は最初の行を使用して解決します。

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **ヘッダーまたはフッターに画像をバインドする**
`(picture)` サフィックスは画像をヘッダーまたはフッターのセクションにバインドします。画像を表示したい位置に `<<node.logo(picture)>>` と記述し、フィールド値としてデータ URI（例: `data:image/png;base64,` に続く画像バイトの Base64 テキスト）を供給します。`data:` プレフィックスなしの純粋な Base64 文字列では画像は埋め込まれません。  
`designer.process()` 後:
1. プレースホルダーは `&G` に置き換えられます。これは標準的なヘッダー/フッタ画像コードです。マーカーがセクション文字列内のコードになるため、`Logo: <<node.logo(picture)>>` のような長いテキスト中に埋め込むことができます。
2. 画像バイトはワークブック内のメディア パートとしてヘッダー/フッタードローイング レイヤーに添付されるため、印刷時にヘッダーまたはフッターに画像が表示されます。

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

印刷される `&G` は Excel がヘッダーを描画する際に解釈する画像コードであり、`logo.png` のバイトが `HeaderFooterPicture.xlsx` に格納され、コードの代わりに画像が印刷されます。  
ヘッダーとフッターの Smart Markers を使用するには、`PageSetup.setHeader` と `PageSetup.setFooter` で左・中央・右の各セクションに `<<Source.Field>>` プレースホルダーを書き込みます。`WorkbookDesigner` の `designer.setEnableHeaderFooterMarkers(true)` を呼び出してから `designer.process()` を実行し、`designer.setDataSource(name, list)`（Getter Bean リスト）または `designer.setJsonDataSource(name, json)` で値を供給します。完成したセクションは `PageSetup.getHeader` と `PageSetup.getFooter` で取得できます。同じデータソースを使用して本体マーカーとヘッダー/フッターのプレースホルダーを 1 回の処理で同時に埋め込めます。画像をバインドする場合は、データ URI 値とともに `(picture)` サフィックスを付加してください。

## 関連記事
- [SmartMarker 単一セル配列レンダリング](/cells/ja/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}