# OVITO_python_tools

OVITO Python RDF 分析與繪圖工具集。

---

## 程式功能說明

| 腳本 | 功能 |
|---|---|
| `rdf_maker.pl` | Perl 生成 RDF 數據 |
| `rdf_plot.py` | Python 繪製 RDF 曲線 |
| `partial_rdf.py` | 部分 RDF 計算 |

### 數據文件

| 文件 | 說明 |
|---|---|
| `Al0_3_dual.cfg` | Al 合金配置文件 |
| `Al0_3_dual.data` | LAMMPS data 文件 |

## 依賴環境

| 項目 | 需求 |
|---|---|
| 語言 | Perl 5.x, Python 3.x |
| 繪圖 | matplotlib |
| 分析 | OVITO Python |

## AI Agent 操控指南

```
任務: 計算並繪製 RDF
步驟:
1. perl rdf_maker.pl 生成 RDF 數據
2. python rdf_plot.py 繪製 RDF 曲線
3. python partial_rdf.py 計算部分 RDF
```
