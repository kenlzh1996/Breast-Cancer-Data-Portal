from pdb import set_trace
from bokeh.models import Whisker, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from Subtype_Average_Plot_Source import jo_Subtype_Avg_Plot_CDS, kr_Subtype_Avg_Plot_CDS, me_Subtype_Avg_Plot_CDS

# constants
SUBTYPE_PLOT_WIDTH = 515
SUBTYPE_PLOT_HEIGHT = 275
five_subtype_colors = ['#E31A1C', '#FB9A99', '#1F78B4', '#A6CEE3','#33A02C']
five_subtypes = ['Basal', 'Her2', 'LumA', 'LumB', 'Norm']

# function call
[jo_subtype_protein_CDS, jo_subtype_mRNA_CDS] = jo_Subtype_Avg_Plot_CDS()
[kr_subtype_protein_CDS, kr_subtype_mRNA_CDS] = kr_Subtype_Avg_Plot_CDS()
[me_subtype_protein_CDS, me_subtype_mRNA_CDS] = me_Subtype_Avg_Plot_CDS()

########################################################################################################################
################################################### Johansson ##########################################################

def jo_Subtype_Plot():
    """ Function that carries bokeh plot configurations"""
    # Initialize the figure object
    jo_subtype_plot_protein = figure(x_range=FactorRange(*jo_subtype_protein_CDS.data["x"]),
                                     title='', x_axis_label='', y_axis_label='protein z-score',
                                     plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    jo_subtype_plot_mrna = figure(x_range=FactorRange(*jo_subtype_mRNA_CDS.data['x']),
                                  title='', x_axis_label='', y_axis_label='mRNA z-score',
                                  plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    # make protein plot
    jo_subtype_plot_protein.circle('x', 'y', source=jo_subtype_protein_CDS,
                                   fill_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                   line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                   legend_group='legend_group')
    jo_subtype_plot_protein.circle('x', 'upper', source=jo_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly
    jo_subtype_plot_protein.circle('x', 'lower', source=jo_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # make mRNA plot
    jo_subtype_plot_mrna.circle('x', 'y', source=jo_subtype_mRNA_CDS,
                                fill_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                legend_group='legend_group')
    jo_subtype_plot_mrna.circle('x', 'upper', source=jo_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly
    jo_subtype_plot_mrna.circle('x', 'lower', source=jo_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # Add error bars
    # protein plot
    Whisker_protein = Whisker(source=jo_subtype_protein_CDS, base="x", upper="upper", lower="lower",
                              line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2))
    Whisker_protein.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    Whisker_protein.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    jo_subtype_plot_protein.add_layout(Whisker_protein)

    # mRNA plot
    Whisker_mrna = Whisker(source=jo_subtype_mRNA_CDS, base="x", upper="upper", lower="lower",
                           line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2))
    Whisker_mrna.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    Whisker_mrna.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    jo_subtype_plot_mrna.add_layout(Whisker_mrna)

    return jo_subtype_plot_protein, jo_subtype_plot_mrna


########################################################################################################################
##################################################### Krug #############################################################

def kr_Subtype_Plot():
    """ Function that carries bokeh plot configurations"""
    # Initialize the figure object
    kr_subtype_plot_protein = figure(x_range=FactorRange(*kr_subtype_protein_CDS.data["x"]),
                                     title='', x_axis_label='', y_axis_label='protein z-score',
                                     plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    kr_subtype_plot_mrna = figure(x_range=FactorRange(*kr_subtype_mRNA_CDS.data['x']),
                                  title='', x_axis_label='', y_axis_label='mRNA z-score',
                                  plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    # make protein plot
    kr_subtype_plot_protein.circle('x', 'y', source=kr_subtype_protein_CDS,
                                   fill_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                   line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                   legend_group='legend_group')
    kr_subtype_plot_protein.circle('x', 'upper', source=kr_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly
    kr_subtype_plot_protein.circle('x', 'lower', source=kr_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # make mRNA plot
    kr_subtype_plot_mrna.circle('x', 'y', source=kr_subtype_mRNA_CDS,
                                fill_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2),
                                legend_group='legend_group')
    kr_subtype_plot_mrna.circle('x', 'upper', source=kr_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly
    kr_subtype_plot_mrna.circle('x', 'lower', source=kr_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # Add error bars
    # protein plot
    Whisker_protein = Whisker(source=kr_subtype_protein_CDS, base="x", upper="upper", lower="lower",
                              line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2))
    Whisker_protein.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    Whisker_protein.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    kr_subtype_plot_protein.add_layout(Whisker_protein)

    # mRNA plot
    Whisker_mrna = Whisker(source=kr_subtype_mRNA_CDS, base="x", upper="upper", lower="lower",
                           line_color=factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2))
    Whisker_mrna.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    Whisker_mrna.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors, factors=five_subtypes, start=1, end=2)
    kr_subtype_plot_mrna.add_layout(Whisker_mrna)

    return kr_subtype_plot_protein, kr_subtype_plot_mrna


########################################################################################################################
##################################################### Mertins ##########################################################

def me_Subtype_Plot():
    """ Function that carries bokeh plot configurations"""
    # Initialize the figure object
    me_subtype_plot_protein = figure(x_range=FactorRange(*me_subtype_protein_CDS.data["x"]),
                                     title='', x_axis_label='', y_axis_label='protein z-score',
                                     plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    me_subtype_plot_mrna = figure(x_range=FactorRange(*me_subtype_mRNA_CDS.data['x']),
                                  title='', x_axis_label='', y_axis_label='mRNA z-score',
                                  plot_height=SUBTYPE_PLOT_HEIGHT, plot_width=SUBTYPE_PLOT_WIDTH)

    # make protein plot
    me_subtype_plot_protein.circle('x', 'y', source=me_subtype_protein_CDS,
                                   fill_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2),
                                   line_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2),
                                   legend_group='legend_group')
    me_subtype_plot_protein.circle('x', 'upper', source=me_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly
    me_subtype_plot_protein.circle('x', 'lower', source=me_subtype_protein_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # make mRNA plot
    me_subtype_plot_mrna.circle('x', 'y', source=me_subtype_mRNA_CDS,
                                fill_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2),
                                line_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2),
                                legend_group='legend_group')
    me_subtype_plot_mrna.circle('x', 'upper', source=me_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly
    me_subtype_plot_mrna.circle('x', 'lower', source=me_subtype_mRNA_CDS, size=0)  # invisible, here only to set initial visible range correctly

    # Add error bars
    # protein plot
    Whisker_protein = Whisker(source=me_subtype_protein_CDS, base="x", upper="upper", lower="lower",
                              line_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2))
    Whisker_protein.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2)
    Whisker_protein.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2)
    me_subtype_plot_protein.add_layout(Whisker_protein)

    # mRNA plot
    Whisker_mrna = Whisker(source=me_subtype_mRNA_CDS, base="x", upper="upper", lower="lower",
                           line_color=factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2))
    Whisker_mrna.upper_head.line_color = factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2)
    Whisker_mrna.lower_head.line_color = factor_cmap('x', palette=five_subtype_colors[0:4], factors=five_subtypes[0:4], start=1, end=2)
    me_subtype_plot_mrna.add_layout(Whisker_mrna)

    return me_subtype_plot_protein, me_subtype_plot_mrna