---
title: サポートされているExcel関数（C++対応）
linktitle: サポートされているExcel関数
type: docs
weight: 10
url: /ja/cpp/supported-formula-functions/
description: Aspose.Cellsを使用して、Excelの式の読み取り、設定、計算をサポートしている関数一覧を示します。
keywords: 数式機能 計算
---

{{% alert color="primary" %}}

Aspose.Cells APIは、多くの標準関数とExcelの組み込み数式をサポートしています。以下はサポートされている関数の一覧です。アルファベット順に並んでいます。

| | | | | | | | | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **[A](#a)** | **[B](#b)** | **[C](#c)** | **[D](#d)** | **[E](#e)** | **[F](#f)** | **[G](#g)** | **[H](#h)** | **[I](#i)** | **[J](#j)** | **[K](#k)** | **[L](#l)** | **[M](#m)** |
| **[N](#n)** | **[O](#o)** | **[P](#p)** | **[Q](#q)** | **[R](#r)** | **[S](#s)** | **[T](#t)** | **[U](#u)** | **[V](#v)** | **[W](#w)** | **[X](#x)** | **[Y](#y)** | **[Z](#z)** |

{{% /alert %}}

Aspose.Cells の数式計算エンジンを使用して、以下の数式および関数の結果を設定、読み取り、および計算することができます。

###### **A**
|**機能**|**概要**|
| :- | :- |
|ABS|**数学および三角関数**: 数の絶対値を返します
|ACCRINT|**金融**: 周期的な利息を支払う証券の支払い済み利息を返します
|ACCRINTM|**金融**: 満期時に利息を支払う証券の支払い済み利息を返します
|ACOS|**数学および三角関数**: 数のarccosineを返します
|ACOSH|**数学および三角関数**: 数の逆双曲線余弦を返します
|ADDRESS|**検索および参照**: ワークシート内の単一のセルへのテキストとしての参照を返します
|AGGREGATE|**数学および三角関数**: リストまたはデータベース内の集計を返します
|AMORDEGRC|**金融**: 減価償却係数を使用して各会計期間の減価償却を返します
|AMORLINC|**金融**: 各会計期間の減価償却を返します
|ANCHORARRAY|**検索および参照**: セル内のダイナミック配列の全範囲を返します
|AND|**論理**: 引数がすべてTRUEの場合、TRUEを返します
|AREAS|**検索および参照**: 参照内の領域の数を返します
|ARRAYTOTEXT|**テキスト**：指定された範囲からテキスト値の配列を返します。
|ASC|**テキスト**: 文字列内の全角（2バイト）の英字またはカタカナを半角（1バイト）の文字に変換します
|ASIN|**数学および三角関数**: 数のarcsineを返します
|ASINH|**数学および三角関数**: 数の逆双曲線正弦を返します
|ATAN|**数学および三角関数**: 数のarctangentを返します
|ATAN2|**数学および三角関数**: x-およびy座標からarctangentを返します
|ATANH|**数学および三角関数**: 数の逆双曲線正接を返します
|AVEDEV|**統計**: データ点の平均絶対偏差を返します
|AVERAGE|**統計**: 引数の平均を返します
|AVERAGEA|**統計**: 数値、テキスト、論理値を含む引数の平均を返します
|AVERAGEIF|**統計**: 指定した条件を満たす範囲内のすべてのセルの平均（算術平均）を返します
|AVERAGEIFS|**統計**: 複数の条件を満たすすべてのセルの平均（算術平均）を返します。

###### **B**
|**機能**|**概要**|
| :- | :- |
|BESSELI|**エンジニアリング**: 変形Bessel関数In(x)を返します
|BESSELJ|**エンジニアリング**: Bessel関数Jn(x)を返します
|BESSELK|**エンジニアリング**: 変更されたベッセル関数 Kn(x) を返します
|BESSELY|**エンジニアリング**: ベッセル関数 Yn(x) を返します
|BETADIST|**互換性**: beta 累積分布を返します
|BETA.DIST|**統計**: beta 累積分布を返します
|BETAINV|**互換性**: 指定された beta 分布の累積分布関数の逆を返します
|BETA.INV|**統計**: 指定された beta 分布の累積分布関数の逆を返します
|BIN2DEC|**エンジニアリング**: 2 進数を 10 進数に変換します
|BIN2HEX|**エンジニアリング**: 2 進数を 16 進数に変換します
|BIN2OCT|**エンジニアリング**: 2 進数を 8 進数に変換します
|BINOMDIST|**互換性**: 個々の項の二項分布確率を返します
|BINOM.DIST|**統計**: 個々の項の二項分布確率を返します
|BITAND|**エンジニアリング**: 2 つの数値のビットごとの AND を返します
|BITLSHIFT|**エンジニアリング**: シフト量ビット分左シフトした値を返します
|BITOR|**エンジニアリング**: 2 つの数値のビットごとの OR を返します
|BITRSHIFT|**エンジニアリング**: シフト量ビット分右シフトした値を返します
|BITXOR|**エンジニアリング**: 2 つの数値の排他的な OR を返します
|BYCOL|**論理**：LAMBDAを各列に適用し、結果の配列を返す
|BYROW|**論理**：LAMBDAを各行に適用し、結果の配列を返す

###### **C**
|**機能**|**概要**|
| :- | :- |
|CEILING|**互換性**: 数値を指定された整数または指定された有意位数の倍数に丸めます
|CEILING.MATH|**数学と三角関数**: 数値を指定された整数または指定された有意位数の倍数に切り上げます
|CEILING.PRECISE|**数学と三角関数**: 数値を指定された整数または指定された有意位数の倍数に丸めます。数値の符号に関係なく、数値は切り上げられます
|CELL|**情報**: セルのフォーマット、位置、または内容に関する情報を返します
|CHAR|**テキスト**: コード番号で指定した文字を返します
|CHIDIST|**互換性**: カイ2乗分布の片側確率を返します
|CHIINV|**互換性**: カイ2乗分布の片側確率の逆を返します
|CHITEST|**互換性**: 独立性の検定を返します
|CHISQ.DIST|**統計**: 累積ベータ確率密度を返します
|CHISQ.DIST.RT|**統計**: カイ2乗分布の片側確率を返します
|CHISQ.INV.RT|**統計**: カイ2乗分布の片側確率の逆を返します
|CHISQ.TEST|**統計**: 独立性の検定を返します
|CHOOSE|**参照と検索**: 値リストから値を選択します
|CHOOSECOLS|**検索と参照**: 配列から指定された列を返します
|CHOOSEROWS|**検索と参照**: 配列から指定された行を返します
|CLEAN|**テキスト**: テキストから非印刷可能な文字を除去します
|CODE|**テキスト**: テキスト文字列内の最初の文字の数値コードを返します
|COLUMN|**検索と参照**: 参照の列番号を返します
|COLUMNS|**検索と参照**: 参照の列数を返します
|COMBIN|**数学と三角関数**: 特定のオブジェクト数に対する組み合わせの数を返します
|COMPLEX|**エンジニアリング**: 実数係数および虚数係数を複素数に変換します
|CONCAT|**テキスト**: 複数の範囲や文字列からテキストを結合しますが、区切り文字やIgnoreEmptyの引数は提供されません。
|CONCATENATE|**テキスト**: 複数のテキストアイテムを一つのテキストアイテムに結合します
|CONFIDENCE|**互換性**: 母集団平均の信頼区間を返します
|CONFIDENCE.NORM|**統計**: 母集団平均の信頼区間を返します
|CONVERT|**エンジニアリング**: 数値を1つの測定システムから別の測定システムに変換します
|CORREL|**統計**: 2つのデータセット間の相関係数を返します
|COS|**数学と三角関数**: 数値の余弦を返します
|COSH|**数学と三角関数**: 数値の双曲線余弦を返します
|COUNT|**統計**: 引数リスト内の数値の数を数えます
|COUNTA|**統計**: 引数リスト内の値の数を数えます
|COUNTBLANK|**統計**: 範囲内の空白セルの数を数えます
|COUNTIF|**統計**: 条件を満たす範囲内のセルの数を数えます
|COUNTIFS|**統計**: 複数の条件を満たす範囲内のセルの数を数えます
|COUPDAYBS|**金融**: クーポン期間の開始から決算日までの日数を返します
|COUPDAYS|**金融**: 決算日を含むクーポン期間の日数を返します
|COUPDAYSNC|**金融**: 決算日から次のクーポン日までの日数を返します
|COUPNCD|**金融**: 決算日の次のクーポン日を返します
|COUPNUM|**金融**: 決算日と償還日の間に支払われるクーポンの数を返します
|COUPPCD|**金融**: 決算日の前のクーポン日を返します
|COVAR|**互換性**: 共分散、対応する偏差の積の平均を返します
|COVARIANCE.P|**統計**: 共分散、対応する偏差の積の平均を返します
|COVARIANCE.S|**統計**: サンプルの共分散、2つのデータセット内の各データ点ペアの偏差の積の平均を返します
|CRITBINOM|**互換性**: 累積二項分布が基準値以下になる最小の値を返します
|CUMIPMT|**財務**: 2つの期間間の累積利息を返します
|CUMPRINC|**財務**: 2つの期間間のローンの累積元本支払額を返します

###### **D**
|**機能**|**概要**|
| :- | :- |
|DATE|**日付と時間**: 特定の日付のシリアル番号を返します
|DATEDIF|**日付と時間**: 2つの日付間の日数、月数、または年数を計算します。この関数は、年齢を計算する必要がある数式で役立ちます。
|DATEVALUE|**日付と時間**: テキスト形式の日付をシリアル番号に変換します
|DAVERAGE|**データベース**: 選択したデータベースエントリの平均値を返します
|DAY|**日付と時間**: シリアル番号を月の日に変換します
|DAYS|**日付と時間**: 2つの日付間の日数を返します
|DAYS360|**日付と時間**: 360日法に基づいて、2つの日付間の日数を計算します
|DB|**財務**: 固定減少残高法を使用して指定された期間の資産の減価償却を返します
|DCOUNT|**データベース**: データベース内の数値を含むセルの数を数えます
|DCOUNTA|**データベース**: データベース内の非空白セルを数えます
|DDB|**財務**: 二重減少残高法または指定した他の方法を使用して、指定された期間の資産の減価償却を返します
|DEC2BIN|**エンジニアリング**: 10進数を2進数に変換します
|DEC2HEX|**エンジニアリング**: 10進数を16進数に変換します
|DEC2OCT|**エンジニアリング**: 10進数を8進数に変換します
|DEGREES|**数学と三角関数**: 弧度法を度数に変換します
|DELTA|**エンジニアリング**: 2つの値が等しいかどうかをテストします
|DEVSQ|**統計**: 偏差の二乗の合計を返します
|DGET|**データベース**: 指定された条件に一致するデータベースから単一のレコードを抽出します
|DISC|**財務**: 証券の割引率を返します
|DMAX|**データベース**: 選択したデータベースエントリから最大値を返します
|DMIN|**データベース**: 選択したデータベースエントリから最小値を返します
|DOLLAR|**テキスト**: $（ドル）通貨形式を使用して、数値をテキストに変換します
|DOLLARDE|**財務**: 分数として表されたドル価格を10進数として表されたドル価格に変換します
|DOLLARFR|**財務**: 10進数として表されたドル価格を分数として表されたドル価格に変換します
|DPRODUCT|**データベース**: データベース内の条件に一致するレコードの特定のフィールドの値を乗算します
|DROP|**検索と参照**：配列の先頭または末尾から指定された行数または列数を除外します。
|DSTDEV|**データベース**: 選択されたデータベースエントリのサンプルに基づいて標準偏差を推定します
|DSTDEVP|**データベース**: 選択したデータベースエントリの母集団に基づく標準偏差を計算します
|DSUM|**データベース**: 条件に一致するデータベースのレコードのフィールド列の数を追加します
|DURATION|**金融**: 定期的な利払いを持つ証券の年間期間を返します
|DVAR|**データベース**: 選択したデータベースエントリのサンプルに基づいて分散を推定します
|DVARP|**データベース**: 選択したデータベースエントリの母集団に基づく分散を計算します

###### **E**
|**機能**|**概要**|
| :- | :- |
|EDATE|**日付と時刻**: 開始日から指定された月数前後の日付のシリアル番号を返します
|EFFECT|**金融**: 有効年率を返します
|ENCODEURL|**Web**: URLエンコードされた文字列を返します
|EOMONTH|**日付と時刻**: 指定された月数前後の月の最終日のシリアル番号を返します
|ERF|**エンジニアリング**: エラーを返します
|ERFC|**エンジニアリング**: 余補間のエラーを返します
|ERROR.TYPE|**情報**: エラータイプに対応する番号を返します
|EVEN|**数学と三角法**: 次の偶数整数までの数値を丸めます
|EXACT|**テキスト**: 2つのテキスト値が同一であるかどうかをチェックします
|EXP|**数学と三角法**: 指定された数値のeの累乗を返します
|EXPONDIST|**互換性**: 指数分布を返します

###### **F**
|**機能**|**概要**|
| :- | :- |
|FACT|**数学と三角法**: 数値の階乗を返します
|FACTDOUBLE|**数学と三角法**: 数値の倍階乗を返します
|FALSE|**論理**: 論理値FALSEを返します
|F.DIST|**統計**: F確率分布を返します
|FDIST|**互換性**: F確率分布を返します
|F.DIST.RT|**統計**: F確率分布を返します
|FILTER|**検索と参照**: 定義した条件に基づいてデータの範囲をフィルタリングします
|FIND|**テキスト**: 他のテキスト値が別のテキスト内にあるかを検索します (大文字と小文字を区別します)
|FINDB|**テキスト**: 他のテキスト値が別のテキスト内にあるかを検索します (大文字と小文字を区別します)
|F.INV.RT|**統計**: F確率分布の逆数を返します
|FINV|**互換性**: F確率分布の逆数を返します
|FISHER|**統計**: フィッシャー変換を返します
|FISHERINV|**統計**: フィッシャー変換の逆数を返します
|FIXED|**テキスト**: 指定した小数点以下の桁数で数値を文字列に書式設定します
|FLOOR|**互換性**: 0に向かって数値を切り捨てます
|FLOOR.MATH|**数学および三角関数**: 指定した桁数または指定した倍数に数値を切り捨てます
|FORECAST|**統計**: 線形トレンド上の値を返します（Excel 2016 では新しい予測関数によりこの関数は FORECAST.LINEAR に置き換えられます）
|FORECAST.LINEAR|**統計**: 既存の値に基づいて将来の値を返します
|FORMULATEXT|**検索と参照**: 指定した参照位置の数式をテキストとして返します
|FREQUENCY|**統計**: 垂直配列として頻度分布を返します
|FV|**金融**: 投資の将来価値を返します
|FVSCHEDULE|**金融**: 一連の複利率を適用した初期元本の将来価値を返します

###### **G**
|**機能**|**概要**|
| :- | :- |
|GAMMA.DIST|**統計**: ガンマ分布を返します
|GAMMADIST|**互換性**: ガンマ分布を返します
|GAMMA.INV|**統計**: ガンマ累積分布の逆数を返します
|GAMMAINV|**互換性**: ガンマ累積分布の逆数を返します
|GAMMALN|**統計**: ガンマ関数の自然対数を返します、��(x)
|GCD|**数学および三角関数**: 最大公約数を返します
|GEOMEAN|**統計**: 幾何平均を返します
|GESTEP|**エンジニアリング**: 数値が閾値より大きいかどうかをテストします
|GETPIVOTDATA|**検索と参照**: PivotTable レポートに格納されているデータを返します
|GROW|
