"""
Script để tạo Workflow Diagram cho Smart Maintenance Booking System (VinFast)
Sử dụng matplotlib để vẽ sơ đồ Current-State Workflow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

def create_workflow_diagram():
    # Tạo figure và axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Màu sắc
    color_normal = '#E8F4F8'  # Xanh nhạt
    color_bottleneck = '#FFE5E5'  # Đỏ nhạt
    color_border = '#2C3E50'
    color_text = '#1A1A1A'
    color_arrow = '#34495E'
    
    # === HEADER ===
    ax.text(8, 9.5, 'CURRENT-STATE WORKFLOW: Đặt Lịch Bảo Dưỡng VinFast (Thủ công)', 
            fontsize=18, weight='bold', ha='center', color=color_text)
    ax.text(8, 9.0, '⏱ Tổng thời gian: 10-15 phút/cuộc gọi | 🔴 = Bottleneck | 🔄 = Handoff Point', 
            fontsize=11, ha='center', color='#555', style='italic')
    
    # === BƯỚC 1: KHÁCH GỌI HOTLINE ===
    box1 = FancyBboxPatch((0.5, 6.5), 2.5, 1.8, 
                          boxstyle="round,pad=0.1", 
                          edgecolor=color_border, 
                          facecolor=color_normal, 
                          linewidth=2)
    ax.add_patch(box1)
    ax.text(1.75, 7.9, 'Bước 1', fontsize=11, weight='bold', ha='center')
    ax.text(1.75, 7.5, 'Khách gọi\nhotline VinFast', fontsize=10, ha='center', va='center')
    ax.text(1.75, 6.9, 'Actor: Khách hàng\n⏱ 1-2 phút', fontsize=8, ha='center', style='italic', color='#555')
    
    # === ARROW 1->2 ===
    arrow1 = FancyArrowPatch((3.0, 7.4), (4.2, 7.4),
                            arrowstyle='->', mutation_scale=20, 
                            linewidth=2, color=color_arrow)
    ax.add_patch(arrow1)
    
    # === BƯỚC 2: THU THẬP THÔNG TIN ===
    box2 = FancyBboxPatch((4.2, 6.5), 2.5, 1.8,
                          boxstyle="round,pad=0.1",
                          edgecolor=color_border,
                          facecolor=color_normal,
                          linewidth=2)
    ax.add_patch(box2)
    ax.text(5.45, 7.9, 'Bước 2', fontsize=11, weight='bold', ha='center')
    ax.text(5.45, 7.5, 'Thu thập thông tin\nxe & yêu cầu', fontsize=10, ha='center', va='center')
    ax.text(5.45, 6.9, 'Actor: CSKH\n⏱ 2-3 phút', fontsize=8, ha='center', style='italic', color='#555')
    ax.text(5.45, 6.6, '🔄 Handoff', fontsize=9, ha='center', color='#E67E22', weight='bold')
    
    # === ARROW 2->3 ===
    arrow2 = FancyArrowPatch((6.7, 7.4), (7.9, 7.4),
                            arrowstyle='->', mutation_scale=20,
                            linewidth=2, color=color_arrow)
    ax.add_patch(arrow2)
    
    # === BƯỚC 3: TRA CỨU LỊCH (BOTTLENECK) ===
    box3 = FancyBboxPatch((7.9, 6.5), 2.5, 1.8,
                          boxstyle="round,pad=0.1",
                          edgecolor='#E74C3C',
                          facecolor=color_bottleneck,
                          linewidth=3)
    ax.add_patch(box3)
    ax.text(9.15, 7.9, 'Bước 3 🔴', fontsize=11, weight='bold', ha='center', color='#C0392B')
    ax.text(9.15, 7.5, 'Tra cứu lịch trống\nxưởng (thủ công)', fontsize=10, ha='center', va='center', weight='bold')
    ax.text(9.15, 6.9, 'Actor: CSKH\n⏱ 4-6 phút', fontsize=8, ha='center', style='italic', color='#C0392B')
    ax.text(9.15, 6.6, 'BOTTLENECK', fontsize=9, ha='center', color='#C0392B', weight='bold')
    
    # === ARROW 3->4 ===
    arrow3 = FancyArrowPatch((10.4, 7.4), (11.6, 7.4),
                            arrowstyle='->', mutation_scale=20,
                            linewidth=2, color=color_arrow)
    ax.add_patch(arrow3)
    
    # === BƯỚC 4: TƯ VẤN QUA ĐIỆN THOẠI (BOTTLENECK) ===
    box4 = FancyBboxPatch((11.6, 6.5), 2.5, 1.8,
                          boxstyle="round,pad=0.1",
                          edgecolor='#E74C3C',
                          facecolor=color_bottleneck,
                          linewidth=3)
    ax.add_patch(box4)
    ax.text(12.85, 7.9, 'Bước 4 🔴', fontsize=11, weight='bold', ha='center', color='#C0392B')
    ax.text(12.85, 7.5, 'Tư vấn qua điện\nthoại & chốt lịch', fontsize=10, ha='center', va='center', weight='bold')
    ax.text(12.85, 6.9, 'Actor: CSKH\n⏱ 3-5 phút', fontsize=8, ha='center', style='italic', color='#C0392B')
    ax.text(12.85, 6.6, 'BOTTLENECK', fontsize=9, ha='center', color='#C0392B', weight='bold')
    
    # === ARROW 4->5 (DOWNWARD) ===
    arrow4 = FancyArrowPatch((12.85, 6.5), (12.85, 5.2),
                            arrowstyle='->', mutation_scale=20,
                            linewidth=2, color=color_arrow)
    ax.add_patch(arrow4)
    
    # === BƯỚC 5: GHI NHẬN VÀO CRM ===
    box5 = FancyBboxPatch((11.6, 3.4), 2.5, 1.8,
                          boxstyle="round,pad=0.1",
                          edgecolor=color_border,
                          facecolor=color_normal,
                          linewidth=2)
    ax.add_patch(box5)
    ax.text(12.85, 4.9, 'Bước 5', fontsize=11, weight='bold', ha='center')
    ax.text(12.85, 4.5, 'Ghi nhận & xác\nnhận vào CRM', fontsize=10, ha='center', va='center')
    ax.text(12.85, 3.9, 'Actor: CSKH\n⏱ 1-2 phút', fontsize=8, ha='center', style='italic', color='#555')
    ax.text(12.85, 3.6, '🔄 Handoff', fontsize=9, ha='center', color='#E67E22', weight='bold')
    
    # === VẤN ĐỀ CHÍNH ===
    problem_box = FancyBboxPatch((0.5, 0.5), 8, 2.2,
                                boxstyle="round,pad=0.15",
                                edgecolor='#E74C3C',
                                facecolor='#FFF5F5',
                                linewidth=2,
                                linestyle='--')
    ax.add_patch(problem_box)
    ax.text(4.5, 2.3, '⚠️ VẤN ĐỀ CHÍNH (BOTTLENECK)', 
            fontsize=12, weight='bold', ha='center', color='#C0392B')
    ax.text(4.5, 1.8, '• Bước 3-4 chiếm 70% thời gian xử lý (7-11 phút/cuộc gọi)', 
            fontsize=9, ha='center', color='#555')
    ax.text(4.5, 1.5, '• Phải mở 3-4 tab để tra lịch nhiều xưởng → Tốn thời gian, dễ nhầm lẫn', 
            fontsize=9, ha='center', color='#555')
    ax.text(4.5, 1.2, '• Giải thích qua điện thoại khó hình dung → Khách hàng phải hỏi lại nhiều lần', 
            fontsize=9, ha='center', color='#555')
    ax.text(4.5, 0.9, '• 35% khách không chốt được lịch ngay → Conversion rate chỉ 65%', 
            fontsize=9, ha='center', color='#555')
    
    # === IMPACT BOX ===
    impact_box = FancyBboxPatch((9, 0.5), 6.5, 2.2,
                               boxstyle="round,pad=0.15",
                               edgecolor='#3498DB',
                               facecolor='#EBF5FB',
                               linewidth=2,
                               linestyle='--')
    ax.add_patch(impact_box)
    ax.text(12.25, 2.3, '📊 BUSINESS IMPACT', 
            fontsize=12, weight='bold', ha='center', color='#2C3E50')
    ax.text(12.25, 1.8, '• 3,000 cuộc gọi/tháng × 10 phút = 500 giờ nhân công/tháng', 
            fontsize=9, ha='center', color='#555')
    ax.text(12.25, 1.5, '• Opportunity cost: Mất 35% conversion do khách "cần suy nghĩ"', 
            fontsize=9, ha='center', color='#555')
    ax.text(12.25, 1.2, '• Customer experience: 15-20% khách up máy do chờ lâu', 
            fontsize=9, ha='center', color='#555')
    ax.text(12.25, 0.9, '• 25% khách gọi lại để đổi lịch → Rework và tốn thêm tài nguyên', 
            fontsize=9, ha='center', color='#555')
    
    # === LEGEND ===
    legend_elements = [
        mlines.Line2D([], [], color=color_border, marker='s', linestyle='None',
                     markersize=12, markerfacecolor=color_normal, label='Bước bình thường'),
        mlines.Line2D([], [], color='#E74C3C', marker='s', linestyle='None',
                     markersize=12, markerfacecolor=color_bottleneck, label='Bottleneck (nghẽn cổ chai)'),
        mlines.Line2D([], [], color='#E67E22', marker='o', linestyle='None',
                     markersize=10, markerfacecolor='#E67E22', label='🔄 Handoff Point'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)
    
    # === FOOTER ===
    ax.text(8, 0.2, 'Vin Smart Future — AI Product Scoping Lab 02 | VinFast Smart Maintenance Booking System',
            fontsize=9, ha='center', color='#7F8C8D', style='italic')
    
    plt.tight_layout()
    return fig

def main():
    print("🎨 Đang tạo workflow diagram...")
    
    # Tạo diagram
    fig = create_workflow_diagram()
    
    # Lưu file với resolution cao
    output_path = '04-workflow-diagram.png'
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Đã lưu diagram tại: {output_path}")
    
    # Hiển thị preview
    print("📊 Đang hiển thị preview...")
    plt.show()
    
    print("\n✨ Hoàn thành! File diagram đã sẵn sàng để nộp bài.")

if __name__ == "__main__":
    main()
