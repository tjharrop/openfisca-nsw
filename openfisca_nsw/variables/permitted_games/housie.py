# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This formula is used to calculate whether an organisation meets criteria for conducting a social housie
class charity_housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a charity housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) * ((organisation('proceeds_to_benefitting_organisation', period) >= parameters(period).permitted_games.housie.min_gross_proceeds_to_benefit_org) * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_expenses_for_conducting_gaming_activity', period) <= parameters(period).permitted_games.housie.max_expenses.charity_housie * organisation('gross_proceeds_from_gaming_activity', period)) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prize_per_session) * (organisation('total_prize_value_from_single_gaming_session', period) <= parameters(period).permitted_games.housie.max_value_of_prizes_per_gross_proceeds * organisation('gross_proceeds_from_gaming_activity', period)) * not_(organisation('more_than_ten_tickets_sold_to_same_player', period)) * organisation('ticket_cost', period) <= parameters(period).permitted_games.housie.max_ticket_cost.charity_housie) * organisation('is_another_gaming_activity_happening', period))


class condition_for_multiple_gaming_activities(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Are eligibility conditions being met for organising another gaming activity while one session of a charity housie is being conducted?"

    def formula(organisation, period, parameters):
        return select(
            [organisation('is_another_gaming_activity_happening', period), not_(organisation('is_another_gaming_activity_happening', period))],
            [(organisation('total_prize_value_from_single_gaming_session') <= parameters(period).permitted_games.housie.max_value_of_prize_per_session), True])


# This formula is used to calculate whether an organisation meets criteria for conducting a social housie
class social_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a social housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) * ((organisation('proceeds_to_benefitting_organisation', period) >= organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.housie.min_gross_proceeds_percent_to_benefit_org))))


# This formula is used to calculate whether an organisation meets criteria for conducting a club bingo
class club_bingo(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a club bingo are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period) * ((organisation('proceeds_to_benefitting_organisation', period) >= organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.housie.min_gross_proceeds_percent_to_benefit_org))))
