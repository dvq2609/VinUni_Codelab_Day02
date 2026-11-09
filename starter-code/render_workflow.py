"""Generate the submitted workflow diagram from synthetic baseline values."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
im = Image.new('RGB', (1800, 1320), '#f4f7fa')
d = ImageDraw.Draw(im)
font_path = 'C:/Windows/Fonts/arial.ttf'
def font(size):
    return ImageFont.truetype(font_path, size)
d.text((80, 50), 'XANH SM | QUY TRÌNH SẠC PIN HIỆN TẠI', font=font(42), fill='#075c51')
d.text((80, 115), 'Baseline giả định cho bài lab - cần người vận hành xác nhận', font=font(25), fill='#526170')
steps = [
    ('01  Kiểm tra pin và ca làm', 'Tài xế / ứng dụng | SOC, ca làm → nhu cầu sạc | 2 phút'),
    ('02  Tự quyết định thời điểm sạc', 'Tài xế | thiếu góc nhìn nhu cầu toàn đội xe | 3 phút'),
    ('03  Chọn trạm và di chuyển', 'Tài xế / bản đồ → trạm sạc | 15 phút'),
    ('04  Chờ trụ và nạp năng lượng', 'Tài xế / trạm | 20 phút chờ + 40 phút sạc'),
    ('05  Trở lại khu vực nhận chuyến', 'Tài xế → hệ thống điều phối | 10 phút'),
]
for i, (title, detail) in enumerate(steps):
    y = 190 + i * 185
    hot = i == 3
    d.rounded_rectangle((100, y, 1700, y + 135), radius=18,
                        fill='#fff0ec' if hot else 'white', outline='#d16b50' if hot else '#d4dfe8', width=3)
    d.text((135, y + 20), title, font=font(31), fill='#923e28' if hot else '#123b47')
    d.text((135, y + 72), detail, font=font(26), fill='#354b5a')
    if i < 4:
        d.line((900, y + 140, 900, y + 172), fill='#188571', width=5)
        d.polygon([(890,y+162),(910,y+162),(900,y+178)], fill='#188571')
d.text((100, 1140), 'BOTTLENECK: nhiều xe cùng đi sạc → chờ trụ, giảm năng lực phục vụ.', font=font(27), fill='#923e28')
d.text((100, 1190), 'Tổng minh họa: 90 phút/lượt. Mục tiêu giảm chờ, không loại bỏ thời gian sạc.', font=font(26), fill='#354b5a')
im.save(root / '04-workflow-diagram.png')
