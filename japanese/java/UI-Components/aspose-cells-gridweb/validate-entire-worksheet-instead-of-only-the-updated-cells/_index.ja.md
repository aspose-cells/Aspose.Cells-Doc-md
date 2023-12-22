---
title: 更新されたセルだけではなくワークシート全体を検証します。
type: docs
weight: 80
url: /ja/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **考えられる使用シナリオ**
デフォルトでは、GridWeb は更新されたセルのみを検証し、ワークシート全体を検証しません。ただし、GridWeb がリクエストをサーバーにポストする前にクライアント側でワークシート全体を検証する場合は、acwmain.js 内の needValidateall 変数を true に設定する必要があります。
##  **更新されたセルだけではなくワークシート全体を検証します。**
次のスクリーンショットは、acwmain.js の needValidateall 変数を示しています。これを true に設定すると、GridWeb は更新されたセルだけでなくワークシート全体を検証します。

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


