package keeper

import (
	sdk "github.com/cosmos/cosmos-sdk/types"
	"github.com/notional-labs/craft/x/exp/types"
)

// GetConstantFee get's the denom from the paramSpace .
func (k ExpKeeper) GetDenom(ctx sdk.Context) (denom string) {
	k.paramSpace.Get(ctx, types.ParamStoreKeyDenom, &denom)
	return
}

// GetParams gets the auth module's parameters.
func (k ExpKeeper) GetParams(ctx sdk.Context) (params types.Params) {
	k.paramSpace.GetParamSet(ctx, &params)
	return
}

func (k ExpKeeper) SetParams(ctx sdk.Context, params types.Params) {
	k.paramSpace.SetParamSet(ctx, &params)
}